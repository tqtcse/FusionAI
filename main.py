from gemini import Gemini_Model
from llama import Llama_Model
from compareAi import Compare_Model



if __name__ == "__main__":
	print("-------------------------   Welcome to FusionAI  ---------------------------\nSelect Model:")
	for model in ["GPT", "Gemini", "Llama", "Claude"]:
		print(f"- {model}")
	print("CompareAI: ")
	print("1. Gemini vs Llama")

	while True:
		command_line = input("\n>")
	#Model
		if command_line == "GPT":
			print("Using GPT Model: ")
			while True:
				user_input = input("GPT> ")

				if user_input.lower() == "exit":
					print("Exiting GPT_Model. Goodbye!")
					break

		elif command_line == "Gemini":
			print("Using Gemini Model: ")
			while True:
				user_input = input("Gemini> ")
				
				if user_input.lower() == "exit":
					print("Exiting Gemini_Model. Goodbye!")
					break

				Gemini_Model.output(user_input)

		elif command_line == "Llama":
			print("Using Llama Model: ")
			while True:
				user_input = input("Llama> ")

				if user_input.lower() == "exit":
					print("Exiting Llama_Model. Goodbye!")
					break

				Llama_Model.output(user_input)

		elif command_line == "Claude":
			print("Using Claude Model: ")
			while True:
				user_input = input("Claude> ")

				if user_input.lower() == "exit":
					print("Exiting Claude_Model. Goodbye!")
					break
		#Compare

		elif command_line == "1":
			print("Comparing Gemini and Llama")

		elif command_line == "exit":
			break
