class EventManagement:
    def __init__(self):
        # Dictionary to store event details (event name -> list of participant tuples)
        self.events = {}

    def add_event(self, event_name):
        """Add a new event."""
        if event_name not in self.events:
            self.events[event_name] = []
            print(f"Event '{event_name}' added successfully!")
        else:
            print(f"Event '{event_name}' already exists!")

    def register_participant(self, event_name, participant_name, contact, department, status="Not Attended"):
        """Register a participant in an event."""
        if event_name in self.events:
            participant = (participant_name, contact, department, status)
            self.events[event_name].append(participant)
            print(f"{participant_name} registered for {event_name}.")
        else:
            print(f"Event '{event_name}' not found!")

    def display_participants(self, event_name):
        """Display all participants in a specific event."""
        if event_name in self.events:
            print(f"Participants in {event_name}:")
            for participant in self.events[event_name]:
                print(participant)
        else:
            print(f"Event '{event_name}' not found!")

    def search_participant(self, participant_name):
        """Search for a participant by name and show their event details."""
        found = False
        for event, participants in self.events.items():
            for p in participants:
                if p[0] == participant_name:
                    print(f"{participant_name} is in {event}: {p}")
                    found = True
        if not found:
            print(f"{participant_name} not found in any event.")

    def mark_attendance(self, event_name, participant_name, status):
        """Mark a participant as 'Attended' or 'Not Attended'."""
        if event_name in self.events:
            for i, participant in enumerate(self.events[event_name]):
                if participant[0] == participant_name:
                    self.events[event_name][i] = (participant[0], participant[1], participant[2], status)
                    print(f"{participant_name} marked as {status}.")
                    return
            print(f"{participant_name} not found in {event_name}.")
        else:
            print(f"Event '{event_name}' not found!")

    def event_summary(self):
        """Generate a summary of total participants in each event."""
        print("\nEvent Summary:")
        for event, participants in self.events.items():
            print(f"{event}: {len(participants)} participants")

# Example Usage
ems = EventManagement()
ems.add_event("Photography Contest")
ems.add_event("Coding Hackathon")
ems.register_participant("Photography Contest", "Alice", "1234567890", "CSE")
ems.register_participant("Photography Contest", "Bob", "9876543210", "ECE")
ems.register_participant("Coding Hackathon", "Charlie", "1122334455", "IT")

ems.display_participants("Photography Contest")
ems.search_participant("Alice")
ems.mark_attendance("Photography Contest", "Alice", "Attended")
ems.event_summary()
