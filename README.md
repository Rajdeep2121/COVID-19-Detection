# COVID-19

The COVID-19 pandemic, also known as the coronavirus pandemic, is an ongoing pandemic of coronavirus disease 2019 (COVID‑19) caused by severe acute respiratory syndrome coronavirus 2 (SARS‑CoV‑2). The outbreak was identified in Wuhan, China, in December 2019.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/COVID-19_Outbreak_World_Map_per_Capita.svg/1200px-COVID-19_Outbreak_World_Map_per_Capita.svg.png" width="50%">
</p>

# Symptoms

Common symptoms include fever, cough, fatigue, shortness of breath, and loss of smell. Complications may include pneumonia and acute respiratory distress syndrome. The time from exposure to onset of symptoms is typically around five days, but may range from two to fourteen days. There is no known vaccine or specific antiviral treatment.

Symptoms of COVID-19 can be relatively non-specific and infected people may be asymptomatic. The two most common symptoms are fever (88 per cent) and dry cough (68 per cent). Less common symptoms include fatigue, respiratory sputum production (phlegm), loss of the sense of smell, loss of taste, shortness of breath, muscle and joint pain, sore throat, headache, chills, vomiting, hemoptysis, and diarrhea.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Symptoms_of_coronavirus_disease_2019_4.0.svg/495px-Symptoms_of_coronavirus_disease_2019_4.0.svg.png" width="50%">
</p>


The WHO says approximately one person in five becomes seriously ill and has difficulty breathing. The U.S. Centers for Disease Control and Prevention (CDC) lists emergency symptoms as difficulty breathing, persistent chest pain or pressure, sudden confusion, difficulty waking, and bluish face or lips; immediate medical attention is advised if these symptoms are present.

# Goal

The intent is to classify the X-Rays into normal lung and COVID-19.

# Thinking Process

The opacities are vague and fuzzy clouds of white in the darkness of the lungs. As the differences between normal and COVID-19 X-Rays were extremely subtle, high contrast images were created to make it relatively easier to classify.


<p align="center">
  <img src="https://healthcare-in-europe.com/media/story_section_image/4670/image-01-marti-beide.jpg" width="50%">
</p>
X-Ray of an infected person exhibits some light patches in the lungs. 

# Training and Testing 

Training with 5216 images.<br>
Testing with 624 images.

# Conclusion

The convolutional neural network produces 0.8670 accuracy. It is a big resource for the doctors working in such dangerous conditions to easily identify this major symptom of COVID-19 by feeding these X-Rays into the neural network.

# Future Work 

1)For this model to be more accurate, we will need more datasets.<br>
2)A user interface can be made in future in order to make things easy.
