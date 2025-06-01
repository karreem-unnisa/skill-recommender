import pandas as pd

# List of skills (you can paste your full list here)
skills = """
3D Modeling
3D Printing
AI
Accounting
Activity Planning
Acupuncture
Administration
Advanced Sewing
Agri-Tech
Agriculture
Agriculture Engineering
Agronomy
Animal Husbandry
Anti-Aging Treatments
App Development
App Ops
Architecture
Aromatherapy
Art
Art Facilitation
Art Instruction
Artistic Design
Audio Editing
Ayurveda
B2B
B2B Sales
Baby Care Knowledge
Baking
Barista Skills
Basic Computing
Basic Sewing
Beauty
Beauty Products
Beauty Services
Beekeeping
Beverage Preparation
Binding
Blockchain
Body Treatments
Branding
Brewing
Business
Business Coaching
Business Consulting
Business Development
Business Management
Business Ownership
Business Planning
Business Strategy
CAD
CAD Design
Calligraphy
Candle Making
Career Coaching
Career Development
Carving
Certification
Chemistry
Child Development
Childcare
Civil Engineering
Clay Craft
Clay Molding
Client Management
Client Relations
Client Service
Cloud Computing
Coaching
Cocktail Mixing
Coding
Cold Chain Management
Collaboration
Color Theory
Comfort Fit
Communication
Community Building
Community Management
Composting Skills
Concierge
Construction
Consulting
Container Gardening
Content
Content Creation
Cooking
Coordination
Copywriting
Corporate Training
Costume Design
Counseling
Couture Techniques
Craft
Craft Curation
Craft Skills
Crafting
Craftsmanship
Creative Design
Creative Direction
Creativity
Crochet
Crowd Engagement
Cryotherapy
Culinary Arts
Cultural Knowledge
Curation
Curriculum Design
Customer Retention
Customer Service
Customization
Cybersecurity
DIY Crafting
DIY Décor Craft
Data Analysis
Data Handling
Delivery
Design
Detail Work
Detailing
Development
Diet Knowledge
Digital Art
Digital Literacy
Digital Marketing
Digital Products
Digital Skills
Digital Teaching
Documentation
Draping
Drawing
Dyeing
E-commerce
E-learning
Eco-Friendly Beauty
Eco-Friendly Design
Eco-Friendly Fabric Knowledge
Eco-Friendly Fabric Sourcing
Eco-friendly Design
Ecology
Editing
Education
Elastic Garment Design
Email Marketing
Embroidery
Energy Audit
Entrepreneurship
Environmental Science
Equipment
Event Management
Event Planning
Export
Fabric Dyeing
Fabric Knowledge
Fabric Selection
Fabric Sourcing
Face Art
Fan Culture
Farming
Fashion
Fashion Design
Fast Painting
Fermentation
Filmmaking
FinTech
Finance
Financial Coaching
Financial Consulting
Financial Planning
Fine Art
Fine Art Knowledge
Fitness Coaching
Fitness Training
Flexibility
Floral Design
Food Processing
Food Safety
Forging
Franchise
Freelancing
Furniture Restoration
Gardening
Gardening Expertise
Gardening Knowledge
Gift Wrapping Knowledge
Glass Work
Gourmet Cooking
Graphic Design
Green Architecture
Grilling
Grooming
Group Management
HR
Hair Care
Hair Extensions
Hair Removal
Hair Styling
Hand Stitching
Haute Couture
Healing
Healing Practices
Health
Health Products
Herbal Knowledge
Herbal Medicine
Horticulture
Hydroponics
Illustration
Inclusive Design
Income Generation
Indoor Farming
Influencer Marketing
Information Gathering
Instruction Design
Instrument Crafting
Insurance
Interior Design
Inventory
Inventory Management
IoT
Japanese Cuisine
Jewelry & Decor Making
Jewelry Design
Knitting
Landscaping
Language Skills
Large-Scale Cooking
Laser Treatments
Leather Craft
Legal
Licensing
Licensing Knowledge
Local Sourcing
Logistics
Luxury Services
Macramé
Makeup
Makeup Application
Management
Market Research
Marketing
Massage
Massage Techniques
Materials Sourcing
Maternity Care
Mechanical Engineering
Medical
Medical Knowledge
Mental Health
Mental Health Coaching
Mentorship
Metal Work
Miniatures
Mobile App Development
Mobile Services
Mobility
Model Making
Molding
Montessori Education
Nail Art
Nail Care
Negotiation
Networking
Niche Skills
Nighttime Care
Nutrition
Nutrition Knowledge
Office Supplies Knowledge
Organic Agri Knowledge
Organic Agriculture
Organic Certification
Organic Chemistry
Organic Fabric Knowledge
Organic Fabric Sourcing
Organic Farming
Organic Farming Knowledge
Organic Food Handling
Organic Knowledge
Organic Lifestyle Knowledge
Organic Material Knowledge
Organic Practices
Organic Product Knowledge
Organic Sourcing
Organization
Packaging
Packaging Design
Painting
Paper Art
Paper Crafting
Parenting
Passive Income
Pastry Design
Patience
Pattern Drafting
Pattern Making
Personal Branding
Personal Development
Personalization
Pest Control
Pet Anatomy
Photography
Piercing
Plant Science
Portfolio Building
Post-production
Postpartum Care
Pottery
Product Curation
Product Customization
Product Design
Product Development
Product Display
Product Formulation
Product Knowledge
Product Sales
Production
Productivity
Programming
Project Management
Proposal Writing
Psychology
Public Relations
Public Speaking
Real Estate
Recipe Development
Recruitment
Recycling
Regional Styles
Remote Work
Renewable Energy
Repair Techniques
Reporting
Research
Resin Casting
Restoration
Retail
Retail Management
Rug Weaving
Rural Mobility
SEO
STEM Education
Safety
Safety Knowledge
Sales
Scent Crafting
Scheduling
Seasonal Crafting
Seed Knowledge
Sewing
Skin Care
Skincare
Skincare Treatments
Sleep Science
Social Media
Social Skills
Software Development
Software Engineering
Software Training
Soil Science
Sourcing
Spa Treatments
Special Needs Expertise
Strategy
Styling
Subscription
Subscription Management
Supply Chain
Sustainability
Sustainability Analysis
Sustainable Cooking
Sustainable Design
Sustainable Materials
Sustainable Product Sourcing
Swimming Knowledge
Tailoring
Tailoring Tech
Tattooing
Tax & Legal
Tax Consulting
Teaching
Tech
Tech Support
Tech Tools
Technology
Textile
Textile Craft
Textile Dyeing
Therapy
Time Management
Traditional Art
Transport
Tutoring
Typography
UX/UI Design
Urban Farming
User Experience
Vegan Baking
Video Content
Video Editing
Video Production
Videography
Virtual Assistance
Voice Talent
Voiceover
Wall Painting
Waste Management
Water Conservation
Water Management
Weaving
Web Analytics
Web Development
Web Management
Weekend Availability
Wellness
Wellness Coaching
Wine Knowledge
Wood Craft
Woodworking
Work-Life Balance
Writing
""".strip().split("\n")  # Replace ... with the full list if needed

# Create DataFrame with placeholders
df = pd.DataFrame(skills, columns=["Skill"])
df["Description"] = ""
df["Resources"] = ""
df["Business Applications"] = ""
df["Avg Monthly Profit (INR)"] = ""

# Save to CSV
df.to_csv("skills_dataset.csv", index=False)

print("Dataset created and saved as 'skills_dataset.csv'")
