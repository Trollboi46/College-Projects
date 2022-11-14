from time import time,sleep
import webbrowser
path = "D:\College\Semester 3\IT Workshop\Group 8 (Academic Chatbot)\ITW Group 8 Final Project\mess menu.pdf"
bot_name = "Admin"

def get_response(msg):
    msg=msg.lower()
    if msg.find('exit') != -1 or msg.find('thank you') != -1 or msg.find('stop') != -1:
        return "Thank you for your time!"
    if msg.find('hi') != -1 or msg.find('hello') != -1:
        return "Hello! How may I help you"
    if (msg.find("intake") != -1 or msg.find("capacity")!= -1 or msg.find("strenght") != -1):
            return "Total Intake in B.Tech. CSE is 223, B.Tech. CSE AI &  ML, CSE DS, CSE HCIG is 66 each"
    if (msg.find("hostel") != -1 and (msg.find("fees")!= -1 or msg.find("fee") != -1)):
            return "Double Seater (ODD SEM): 81000/-\n\n             Double Seater (EVEN SEM): 35000/-\n\n             Four-Seater (ODD SEM) : 66000/- \n\n             Four-Seater (ODD SEM) : 27500/-"
    if (msg.find("photo") != -1 or msg.find("gallary"))!= -1 :
            return "Please visit the site: https://iiitn.ac.in/photo-gallery-album/upcoming-campus-photo/"
    if (msg.find("cutoff") != -1):
            return "For CSE: OR:19262 CR:29245\n\n             For ECE: OR:29807 CR:45328\n\n             Please visit the link for detail information: https://iiitn.ac.in/Cut%20off%202021-2022.pdf"
    if (msg.find("placement") != -1) or (msg.find("statistics") != -1):
            return "For 2022 Batch:\n\n            Highest Package: 40 LPA \n\n            Average Package: 12.04 LPA\n\n            Please visit https://www.iiitn.ac.in/page/placement-statistics/45/ for more information"
    if msg.find("techfest")!=-1 or msg.find("fest")!=-1 or msg.find("cultural")!=-1:
        return """IIITN has two events which are hosted each year in February and October. The Techfest, know as\n\n            Tantrafiesta brings an array of competitions from robotics to debate.\n\n            The Cultural fest, known as Abivyakti challenges students to bring out their inner creativitty in competitons \n\n            like dance, drama, singing,etc."""
    if (msg.find("document") != -1 or msg.find("documents") != -1):
            return "ID Proof -- Aadhaar Card (mandatory) / PAN Card  / Driving License / Voter ID card\n\n             Address Proof (Any One)-- Electricity bill / Bank Passbook / Aadhar card / Rent agreement"
    if msg.find("fee") != -1 or msg.find("fees") != -1:
        return "Odd Semester Fees = 123500\n            Even Semester Fees=123500\n            Total Fees= 247000 \n            For more details visit the link:https://www.iiitn.ac.in/page/undergraduate-btech/40/"
    if msg.find("how") != -1 and msg.find("are")!=-1 and msg.find("you")!=-1:
        return "I am fine! Please ask relevant questions"
    if msg.find("syllabus") != -1 and msg.find("cse")!=-1:
        return "Syllabus for CSE core branch is as follows\n            Data Structures and Algorithm\n            Object Oriented Programming\n            Artificial Intelligence\n            Machine Learning\n            Web Development\n            Android Development\n            "
    if msg.find("syllabus") != -1 and msg.find("ece")!=-1:
        return "Syllabus for ECE Core branch is as follows\n            Analog and Integrated Circuits\n            Microprocessor and Interfacing\n            Signals and Systems\n            Digital Electronics\n            Network Theory"
    if msg.find("stay")!=-1 or msg.find("hotel")!=-1 or msg.find("nearby hotels")!=-1:
        return "Here is a list of the hotels nearby with their phone number:\n\n            1.OYO 30071 Hotel Samruddhi : 01246201126\n\n            2.Hotel Regency : 09325777205\n\n            3.OYO Flagship 83338 Jamtha Hotel Guest House : 01246201126\n\n            4.Hotel Mayur"
    if(msg.find("admission") !=-1 and msg.find("btech") ==-1 and msg.find("mtech")==-1 and msg.find("phd")==-1 and msg.find("diploma")==-1):
        return "What specifically you want to ask about Admission ?"
    if msg.find("mess")!=-1 or msg.find("dining")!=-1 or msg.find("food")!=-1:
        sleep(1)
        webbrowser.open_new(path)
        return "There are four dining halls for all the students in hostel block A.\n\n             The mess serves a variety of food and the menu is opened in the browser"
    if (msg.find('procedure') != -1 or msg.find('guideline')) and msg.find('btech') != -1:
            return "Procedure for B.Tech admission is as follows :\n\n           Candidates shall be offered colleges based on their All India Ranks in JEE Main.\n\n           To get admission in IIIT Nagpur, score a good rank in JEE Main and apply through JoSAA ."
    elif (msg.find('procedure') != -1 or msg.find('guideline')) and msg.find('mtech') != -1:
            return "Procedure for M.Tech admission is as follows : "
    elif (msg.find('procedure') != -1 or msg.find('guideline')) and msg.find('diploma') != -1:        
            return "Procedure for Diploma admission is as follows : "
    else:
        return "Sorry, we cannot answer this question.We will contact you soon for clarifying this doubt if relevant."
