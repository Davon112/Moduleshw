# Question 1
import mood_responses

mood = input("How are you feeling today?")
print(mood_responses.mood_responses(mood))

# Question 2 
import text_utils as reverse
text = "Hannah"
reversed_text = reverse.reverse_string(text)
print("Reversed:", reversed_text)