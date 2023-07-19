# Automatic-Accident-Detection

Due the more road accident takes place in various cities. Nowadays the cause of death increasing more by accident. If an accident met in a national highway roads no one 
there to rescue the person to met with an accident this is due to lack of emergency facilities and rescue team to overcome these drawback we made a system which on occurence of an accident, takes the location of accident and find nearest hospitals, chooses the closest of them and sends them a message regarding the location of accident. It can used to protect the people from the risk as soon as possible after occurrence the accident wasting a time may leads to death. The location of the accident place will be detect by geocoder function.   
This is a prototype which takes the input in form of latitude and longitude and finds the nearest location of hospital from the given dataset of hospitals. For the time being, as the contact number of hospitals are not given, we used a dummy number to get the message regarding the accident.

## Installation

1. Download the zip file or git clone the repository.
2. Unzip the hospital_data file.
3. Install the requirements.
4. Use your twilio api keys.
5. Run the program.

## Flow Diagram

![FlowChart](https://github.com/vivekkumar7089/Automatic-Accident-Detection/assets/60113444/9fc9064e-eb62-4bf6-8d0c-5491d5867a22)


## Proposed Followup

- We would need a hardware which can be integrated in every vehicle which detects the accident and send the current location the backend server for the following process.
- We can also make a trigger function which works as follows:
    - If an accident occurs, it pops up a notification on the smartphone of the person.
    - It will let choose the person to continue the followup process or to cancel it if it is not a major accident or a malfunction.
    - It will also have a time limit so that if no response is provided, it automatically continues the followup process.
- To make this a successful prototype, we would need to integrate the hospitals too in this.
- We can make a different dashboard which will keep the information regarding the availability of emergency ward and available ambulances at a hospital.
- We can then change the finding best hospital function to choose the hospital considering availability also.
- We can implement the same system for the police stations so that the information regarding accident can be conveyed at the earliest.
- The information regarding which hospital is covering the accident can also be sent to the police so that they can carry out the legal formalities.
- A dashboard can be made which can tell the location of ambulance and the accident location for the police so that they can track it.
- A system can also be made which informs the family or guardian or relative of the person about the accident.

## Major Problems

#### Integration with existing systems
For your product to be effective, it will need to integrate with existing hospital and police station infrastructure. It will be a challenging task as different organizations may use different technologies and protocols.

#### Communication and coordination
Effective communication and coordination between police and hospitals are essential for a seamless response to accidents. Establishing clear lines of communication, defining roles and responsibilities, and addressing any potential conflicts or misunderstandings between these entities can be a challenging task.

#### Adaptability 
Adaptability can indeed be a significant challenge when selling an automatic accident detection system to hospitals. Hospitals are complex organizations with established processes and protocols for handling emergencies, and introducing a new system may encounter resistance or face certain barriers.
  
