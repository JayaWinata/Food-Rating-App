As a final project for the AI course, this application aims to develop a comprehensive tool for assessing the nutritional quality of food. By utilizing fuzzy logic, the app will provide users with personalized recommendations to improve their dietary habits.
The fuzzy logic algorithm used in this project is a fairly simple yet effective algorithm for providing qualitative assessments based on numerical inputs. Generally, this algorithm consists of several stages:
1. Fuzzification: The process of converting numerical values (e.g., carbohydrate, protein, and fat values) into membership values in a fuzzy set. The membership value indicates the degree to which a numerical value belongs to a particular fuzzy set.
2. Inference: The process of applying fuzzy rules to map input membership values to output membership values. Fuzzy rules typically take the form of "If condition A then consequence B," where condition A and consequence B are expressed in terms of fuzzy sets.
3. Defuzzification: The process of converting the output membership value into a numerical value or linguistic label. This numerical value is then interpreted as the overall health value of the food.

Key Features:
- Food Quality Assessment: Utilizes fuzzy logic to evaluate the nutritional balance of food based on its carbohydrate, protein, and fat content.
- Personalized Recommendations: Offers tailored dietary advice to users, suggesting adjustments in macronutrient intake to achieve optimal health.

Objectives:
1. Successfully integrate fuzzy logic concepts to model the subjective and uncertain nature of food quality assessment.
2. Create an efficient algorithm that accurately calculates the health value of food based on its nutritional composition.
3. Develop a system that generates relevant and actionable dietary recommendations for users.

Technologies:
- Python
- Tkinter
