import os
import warnings
warnings.filterwarnings('ignore')

from IPython.display import Markdown


from crewai import Crew
from agents import planner, writer, editor
from tasks import plan, write, edit

os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'

crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=2
)

result = crew.kickoff(inputs={"topic": "Artificial Intelligence"})
Markdown(result)
