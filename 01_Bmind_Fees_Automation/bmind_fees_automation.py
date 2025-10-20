# STEP 1 - Test loading environment variables

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Read values
stripe_key = os.getenv("STRIPE_API_KEY")
bubble_url = os.getenv("BUBBLE_API_URL")

print("✅ Environment loaded successfully!")
print("Stripe Key (hidden preview):", stripe_key[:8] + "...")
print("Bubble URL:", bubble_url)
