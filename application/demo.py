"""Demo routes."""
from flask import render_template
from flask import Blueprint, request
from .models import Question, FeedItem

demo_bp = Blueprint('demo_bp', __name__)


@demo_bp.route("/", methods=['GET'])
def demo():
    """Demo Homepage."""
    return render_template('/demo.html',
                           template="demo-template")


@demo_bp.route("/login-demo/", methods=['GET'])
def login():
    """Login page."""
    return render_template('/login.html',
                           template="login-template")


@demo_bp.route("/signup-demo/", methods=['GET'])
def signup():
    """Signup page."""
    return render_template('/signup.html',
                           template="signup-template")


@demo_bp.route("/signup-complete/", methods=['GET'])
def signup_complete():
    """Signup complete page."""
    return render_template('/signupcomplete.html',
                           template="signup-template")


@demo_bp.route("/feed/", methods=['GET'])
def feed():
    """Feed page."""
    feedItems = FeedItem.query.all()
    items = [item.__dict__ for item in feedItems]
    return render_template('/feed.html',
                           title='Product/Market Fit Workshop',
                           description='Welcome to the Product/Market Fit Workshop where you’ll learn all about how to make sure people will buy what you’re selling. This workshop is full of interactive exercises that will help you create a strategy on your product/market fit.',
                           items=items,
                           template="feed-template")


@demo_bp.route("/question/<int:num>/", methods=['GET'])
def question(num):
    """Question and answer page."""
    if request.method == 'GET':
        questionGroup = Question.query.filter(Question.num == num).from_self().all()
        answers = [answer.value for answer in questionGroup if '_text' in answer.variable]
        responses = [response.value for response in questionGroup if '_response' in response.variable]
        tooltips = [response.value for response in questionGroup if '_hover' in response.variable]
        questionType = questionGroup[0].question_type
        if questionType == 'Multiple Choice':
            return render_template('/question-multiplechoice.html',
                                   question=questionGroup[0].question,
                                   choices=answers,
                                   responses=responses,
                                   tooltips=tooltips,
                                   # variables=variables,
                                   explanation=questionGroup[0].info,
                                   template="question-multiplechoice")
        return render_template('/question-freeform.html',
                               question=questionGroup[0].question,
                               choices=answers,
                               responses=responses,
                               tooltips=tooltips,
                               # variables=variables,
                               explanation=questionGroup[0].info,
                               template="question-freeform")
