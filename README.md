<p align="center">
  <img src="static/images/logo.png" width="100" alt="EduStream logo" />
</p>

<h1 align="center">EduStream</h1>
<p align="center"><b>A free learning platform: video tutorials, quizzes, and peer forums in one Streamlit app.</b></p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/python-3.8+-3776AB?logo=python&logoColor=white">
  <img alt="Streamlit" src="https://img.shields.io/badge/app-Streamlit-FF4B4B?logo=streamlit&logoColor=white">
  <a href="https://edustream-jjsajdx7oxaqm7sa2m7thn.streamlit.app/"><img alt="Live demo" src="https://img.shields.io/badge/demo-live-brightgreen"></a>
</p>

EduStream pulls together three real external services into one page:
YouTube for tutorials, the Open Trivia Database for quizzes, and Disqus
for discussion, so a learner has content, self-testing, and a place to
ask questions without leaving the app.

## Features

- **Tutorials**: pulls the latest videos from a YouTube channel via the
  YouTube Data API and embeds them in-app.
- **Quizzes**: fetches multiple-choice questions from the
  [Open Trivia DB](https://opentdb.com/) API, cached for a minute to
  avoid hitting rate limits.
- **Forums**: a Disqus thread embedded per page for peer discussion.
- **Personalized learning**: a recommendation stub
  (`ai/recommender.py`) that takes a user's stated learning style and
  topics and suggests what to study next. It's currently a rule-based
  placeholder rather than a trained model, an intentional extension
  point for plugging in a real recommender later.

## Try it live

[edustream-jjsajdx7oxaqm7sa2m7thn.streamlit.app](https://edustream-jjsajdx7oxaqm7sa2m7thn.streamlit.app/)

## Running it locally

```bash
git clone https://github.com/Heet852003/EduStream.git
cd EduStream
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Open http://localhost:8501 and use the sidebar to switch between
Tutorials, Quizzes, Forums, and Personalized Learning.

## Repository layout

```
app.py              page routing and the home/personalized-learning views
pages/tutorials.py   YouTube Data API integration
pages/quizzes.py     Open Trivia DB integration
pages/forums.py      Disqus embed
ai/recommender.py    the learning-path recommendation stub
static/              CSS and images
```

## Contributing

Fork the repo, branch, commit, and open a pull request, standard GitHub
flow.
