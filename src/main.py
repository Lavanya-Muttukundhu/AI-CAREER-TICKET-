import uuid
import os
import json
from datetime import datetime
from classifier import categorize_ticket

def save_ticket_to_file(ticket_data):
    folder = 'tickets'
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = os.path.join(folder, f"ticket_{ticket_data['ticket_id']}.json")
    with open(filename, 'w') as f:
        json.dump(ticket_data, f, indent=4)

def create_ticket():
    print("--- AI Ticket System Milestone 2 ---")
    user_input = input("Please describe your issue: ").strip()

    # ERROR HANDLING: Milestone 2 Requirement
    if len(user_input) < 10:
        print("Error: Please provide a more detailed description (min 10 chars).")
        return

    category, priority = categorize_ticket(user_input)

    ticket = {
        "ticket_id": str(uuid.uuid4())[:8],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "description": user_input,
        "category": category,
        "priority": priority,
        "status": "Open"
    }

    print(f"\nAI analyzed your issue as: {category} with {priority} priority.")
    save_ticket_to_file(ticket)
    print("Successfully saved to /tickets folder.")

if __name__ == "__main__":
    create_ticket()
    