# Firebase prerequisites
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Referencing the JSON key ("serviceAccountKey.json")
cred = credentials.Certificate('serviceAccountKey.json')


# Admin priviledges to the database, connecting the database URL to the program
firebase_admin.initialize_app(cred, {
    'database_url': 'https://fbla-47b73-default-rtdb.firebaseio.com'
})

ref = db.reference('py/')
companies_ref = ref.child('companies')
companies_ref.set({
  "TechEdu Solutions": {
    "website": "www.techedusolutions.com",
    "contact": "Sarah Anderson",
    "email": "sarah@techedusolutions.com",
    "phone": "555-123-4567",
    "description": "TechEdu Solutions provides comprehensive technology solutions for CTE programs, including virtual labs, interactive learning platforms, and student assessment tools."
  },
  "InnoSkillsTech": {
    "website": "www.innoskillstech.io",
    "contact": "Michael Carter",
    "email": "michael@innoskillstech.io",
    "phone": "555-234-5678",
    "description": "InnoSkillsTech specializes in developing cutting-edge skill assessment software, helping CTE directors track student progress and tailor their programs to individual needs."
  },
  "VirtuLearn Systems": {
    "website": "www.virtulearnsystems.com",
    "contact": "Emily Rodriguez",
    "email": "emily@virtulearnsystems.com",
    "phone": "555-345-6789",
    "description": "VirtuLearn Systems offers virtual reality (VR) educational experiences for CTE programs, enhancing hands-on learning in a simulated environment."
  },
  "EduTrack Innovations": {
    "website": "www.edutrackinnovations.net",
    "contact": "Jason Turner",
    "email": "jason@edutrackinnovations.net",
    "phone": "555-456-7890",
    "description": "EduTrack Innovations provides a comprehensive tracking and reporting system, allowing CTE directors to monitor student performance and program effectiveness."
  },
  "CodeCrafters": {
    "website": "www.codecrafters.com",
    "contact": "Lisa Johnson",
    "email": "lisa@codecrafters.com",
    "phone": "555-567-8901",
    "description": "CodeCrafters specializes in coding and programming resources for CTE programs, offering a platform for students to develop technical skills."
  },
  "SimuSkill Technologies": {
    "website": "www.simuskilltech.co",
    "contact": "Ryan Miller",
    "email": "ryan@simuskilltech.co",
    "phone": "555-678-9012",
    "description": "SimuSkill Technologies provides realistic simulation software for CTE programs, allowing students to practice skills in a risk-free virtual environment."
  },
  "TechTutorHub": {
    "website": "www.techtutorhub.com",
    "contact": "Jessica Lee",
    "email": "jessica@techtutorhub.com",
    "phone": "555-789-0123",
    "description": "TechTutorHub offers a comprehensive online tutoring platform, connecting CTE students with experienced industry professionals for personalized guidance."
  },
  "SkillForge Solutions": {
    "website": "www.skillforge.net",
    "contact": "Brian Adams",
    "email": "brian@skillforge.net",
    "phone": "555-890-1234",
    "description": "SkillForge Solutions provides skill development programs for CTE, offering a range of courses in areas such as IT, healthcare, and engineering."
  },
  "EduTech Innovators": {
    "website": "www.edutechinnovators.org",
    "contact": "Megan Taylor",
    "email": "megan@edutechinnovators.org",
    "phone": "555-901-2345",
    "description": "EduTech Innovators focuses on integrating the latest educational technologies into CTE programs, enhancing the learning experience for students."
  },
  "DigitalDesign Pro": {
    "website": "www.digitaldesignpro.com",
    "contact": "Eric Chang",
    "email": "eric@digitaldesignpro.com",
    "phone": "555-012-3456",
    "description": "DigitalDesign Pro offers graphic design and multimedia tools tailored for CTE programs, empowering students to unleash their creativity."
  },
  "RoboWorks Industries": {
    "website": "www.roboworksindustries.com",
    "contact": "Rachel Simmons",
    "email": "rachel@roboworksindustries.com",
    "phone": "555-123-4567",
    "description": "RoboWorks Industries specializes in robotics education, providing kits and software for hands-on learning in STEM-focused CTE programs."
  },
  "DataDive Analytics": {
    "website": "www.datadiveanalytics.com",
    "contact": "Kevin Wilson",
    "email": "kevin@datadiveanalytics.com",
    "phone": "555-234-5678",
    "description": "DataDive Analytics offers data analysis tools and training for CTE programs, preparing students for careers in data science and analytics."
  },
  "CyberGuard Systems": {
    "website": "www.cyberguardsystems.com",
    "contact": "Angela Martinez",
    "email": "angela@cyberguardsystems.com",
    "phone": "555-345-6789",
    "description": "CyberGuard Systems provides cybersecurity education solutions, including simulations and training modules for CTE programs."
  },
  "FutureBuilders Tech": {
    "website": "www.futurebuilderstech.org",
    "contact": "Daniel Parker",
    "email": "daniel@futurebuilderstech.org",
    "phone": "555-456-7890",
    "description": "FutureBuilders Tech focuses on emerging technologies, offering CTE programs resources to explore innovations in AI, blockchain, and more."
  },
  "SkillSync Academy": {
    "website": "www.skillsyncacademy.com",
    "contact": "Michelle Carter",
    "email": "michelle@skillsyncacademy.com",
    "phone": "555-567-8901",
    "description": "SkillSync Academy provides synchronized learning experiences, integrating real-world projects into CTE curriculum to enhance practical skills."
  },
  "TechHub Connect": {
    "website": "www.techhubconnect.net",
    "contact": "Jonathan Baker",
    "email": "jonathan@techhubconnect.net",
    "phone": "555-678-9012",
    "description": "TechHub Connect offers a collaborative platform for CTE programs, facilitating communication and resource sharing among educators and students."
  },
  "InnoTech Solutions": {
    "website": "www.innotechsolutions.com",
    "contact": "Michelle Chang",
    "email": "michelle@innotechsolutions.com",
    "phone": "555-123-4567",
    "description": "InnoTech Solutions specializes in innovative software solutions for businesses, optimizing processes and enhancing productivity."
  },
  "EcoGrowth Ventures": {
    "website": "www.ecogrowthventures.com",
    "contact": "Alex Rodriguez",
    "email": "alex@ecogrowthventures.com",
    "phone": "555-987-6543",
    "description": "EcoGrowth Ventures is dedicated to promoting sustainable practices, offering eco-friendly products and consulting services for businesses seeking to go green."
  },
  "TechInnovate Solutions": {
    "website": "www.techinnovatesolutions.com",
    "contact": "Alexandra Smith",
    "email": "alexandra@techinnovatesolutions.com",
    "phone": "555-789-0123",
    "description": "TechInnovate Solutions pioneers innovative technology solutions for CTE programs, offering a wide range of cutting-edge tools and platforms to enhance the learning experience for students."
  },
  "HealthHub Technologies": {
    "website": "www.healthhubtech.com",
    "contact": "Dr. Kevin Patel",
    "email": "kevin@healthhubtech.com",
    "phone": "555-234-5678",
    "description": "HealthHub Technologies leverages cutting-edge technology to improve healthcare outcomes, offering solutions for patient engagement and remote monitoring."
  },
  "FutureFarm Innovations": {
    "website": "www.futurefarminnovations.com",
    "contact": "Sarah Mitchell",
    "email": "sarah@futurefarminnovations.com",
    "phone": "555-345-6789",
    "description": "FutureFarm Innovations pioneers smart agriculture solutions, integrating technology to enhance crop yields and sustainability."
  },
  "NanoTech Dynamics": {
    "website": "www.nanotechdynamics.com",
    "contact": "Dr. Michael Wong",
    "email": "michael@nanotechdynamics.com",
    "phone": "555-876-5432",
    "description": "NanoTech Dynamics specializes in nanotechnology research and development, creating innovative solutions for various industries."
  },
  "SkyLink Robotics": {
    "website": "www.skylinkrobotics.com",
    "contact": "Lisa Taylor",
    "email": "lisa@skylinkrobotics.com",
    "phone": "555-567-8901",
    "description": "SkyLink Robotics designs and manufactures cutting-edge robotic systems for industrial automation and exploration."
  },
  "FinanceFleet Solutions": {
    "website": "www.financefleet.com",
    "contact": "David Reynolds",
    "email": "david@financefleet.com",
    "phone": "555-678-9012",
    "description": "FinanceFleet Solutions offers comprehensive financial management tools for businesses, optimizing budgeting and expense tracking."
  },
  "SolarCraft Innovations": {
    "website": "www.solarcraftinnovations.com",
    "contact": "Sophie Reynolds",
    "email": "sophie@solarcraftinnovations.com",
    "phone": "555-567-8901",
    "description": "SolarCraft Innovations harnesses solar energy for sustainable solutions, offering solar power systems and consulting services."
  }
})


handle = db.reference('py/users/vgowda')

print(ref.get())
