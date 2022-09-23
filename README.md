# Seizure Predictor
Repo for seizure predictor project

Epilepsy is a chronic neurologic disorder that causes repeated seizure activity. In 2015, 1.2% of the US population had epilepsy that is about 3.4 million people (CDC, 2020). The World Health Organization estimates 50 million people worldwide have epilepsy. The risk of premature death in people with epilepsy is up to three times higher than the general population (WHO, 2022). 

When someone has a seizure, their body typically convolutes and they are no longer in control of their motor functions, this can lead to fall, head trauma, drowning, and other injuries. Alerting a person before a seizure occurs could allow them time to get to a safe space before they lose control of their motor functions. Realtime or predictive alerting could drastically decrease the risk of injury during a seizure.  

(2020, September 30). Epilepsy Data and Statistics. The Center for Disease Control (CDC). https://www.cdc.gov/epilepsy/data/index.html
(2022, February 9). Epilepsy. The World Health Organization (WHO).  https://www.who.int/news-room/fact-sheets/detail/epilepsy

A seizure detection system will monitor a user’s characteristics such as heart rate, oxygen level, sleep pattern, and physical movements. The system will analyze these inputs to establish a unique pattern of normal behavior, also known as a signature. After establishing a signature, the system will determine deviations from the signature and attempt to predict a seizure occurrence. The prediction alert will be sent to the user and caregivers to ensure no additional harm occurs. Once a prediction or identification of a seizure occurs the users will be able to confirm or refute the prediction and the system will be able to improve precision of future predictions based on feedback from users.  

The physical structure is envisioned to be a software application used on a smart phone or smart watch. The application will take input from external devices like a user’s smart watch and camera. The application will allow the user to interact with it through a user interface. The user interface will send notifications when a seizure event is likely to occur and take input from the user to confirm the accuracy of prediction. 

![image](https://user-images.githubusercontent.com/47536604/192046546-40715d8e-cee7-4586-aebf-7d0dc59523a5.png)

## Running the code
1. Clone the repository.
2. Put the data file in the repository folder.
3. Training the code:
    - To train the code run the following command: `python seizure_predictor.py train [num_data_files]`
4. Testing the code:
    - To test the run the following command: `python seizure_predictor.py predict`

