import os
from dotenv import load_dotenv
load_dotenv()

test = os.getenv('SECRET_KEY')
print(test)

