import datetime

class Campaign:
    def __init__(self, name, budget, platform):
        self.name = name
        self.budget = budget
        self.platform = platform

        self.created = datetime.datetime.now()
        self.leads = self.conversions = self.revenue = 0

    def update(self, leads=0, conversions=0, revenue=0):
        self.leads += leads
        self.conversions += conversions
        self.revenue += revenue

    def rate(self):
        return round(self.conversions / self.leads * 100, 2) if self.leads else 0
    
    def cpl(self):
        return round(self.budget / self.leads, 2) if self.leads else 0
    
    def roi(self):
        return round((self.revenue - self.budget) / self.budget * 100, 2) if self.budget else 0

    def __str__(self):
        return (f"Campaign: {self.name}\n"
                f"Platform: {self.platform}\n"
                f"Budget: ${self.budget}\n"
                f"Leads: {self.leads}\n"
                f"Conversions: {self.conversions}\n"
                f"Revenue: ${self.revenue}\n"
                f"Conversion Rate: {self.rate()}%\n"
                f"CPL: ${self.cpl()}\n"
                f"ROI: {self.roi()}%")

class MarketingApp:
    def __init__(self):
        self.campaigns = []
    
    def menu(self):
        while True:
            print("\n---Welcome to MASTER MARKETING SYSTEM---")
            print("1. Create Campaign")
            print("2. View Campaigns")
            print("3. Update Metrices")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.create_campaign()
            elif choice == '2':
                self.view_campaigns()
            elif choice == '3':
                self.update_campaign()
            elif choice == '4':
                break
            else:
                print("Invalid option. Please try again.")

    def create_campaign(self):
        print("\nCREATE CAMPAIGN")
        name = input("Campaign Name: ")
        budget = float(input("Budget: "))
        platform = input("Platform: ")
        campaign = Campaign(name, budget, platform)
        self.campaigns.append(campaign)
        print("Campaign created successfully.")
    
    def view_campaigns(self):
        if not self.campaigns:
            print("\nNo campaigns available.")
            return
        print("\nCAMPAIGNS:")    
        for campaign in self.campaigns:
            print(campaign)
            print("-" * 30)

    def update_campaign(self):
        if not self.campaigns:
            print("\nNo campaigns available.")
            return
        name = input("\nEnter campaign name to update: ")
        for campaign in self.campaigns:
            if campaign.name == name:
                leads = int(input("Leads: "))
                conversions = int(input("Conversions: "))
                revenue = float(input("Revenue: "))
                campaign.update(leads, conversions, revenue)
                print("Campaign updated successfully.")
                return
        print("Campaign not found.")

if __name__ == "__main__":
    app = MarketingApp()
    app.menu()
