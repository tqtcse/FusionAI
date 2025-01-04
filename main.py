from gemini import Gemini_Model
from llama import Llama_Model
from gpt import GPT_Model
from compareAI import Compare_Model



if __name__ == "__main__":
	while True:
		print("-------------------------   Welcome to FusionAI  ---------------------------\nSelect Model:")
		for model in ["GPT", "Gemini", "Llama", "Claude"]:
			print(f"- {model}")
		print("CompareAI: ")
		print("1. Two Model")
		print("2. All Model")

	
		command_line = input("\n>")

	#Model

		if command_line == "GPT":
			while True:
				print("Using GPT Model: ")
				
				user_input = input("GPT> ")

				if user_input.lower() == "exit":
					print("Exiting GPT_Model. Goodbye!")
					break

				GPT_Model.output(user_input)

		elif command_line == "Gemini":
			while True:
				print("Using Gemini Model: ")
				
				user_input = input("Gemini> ")
					
				if user_input.lower() == "exit":
					print("Exiting Gemini_Model. Goodbye!")
					break

				Gemini_Model.output(user_input)

		elif command_line == "Llama":
			while True:
				print("Using Llama Model: ")
				
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
			print("Comparing Two Model Mode: ")
			print("1. GPT vs Gemini:\n2. GPT vs LLama:\n3. Gemini vs Llama")
			while True:
				user_input = input("CompareModel> ")

				if user_input == "exit":
					print("Exiting Compare Mode.")
					break

				if user_input == "1":
					while True:
						print("GPT vs Gemini: ")

						user_input = input("GPTvsGemini> ")
						if user_input == "A":
							Compare_Model.analyzeOutput(compare_Output)
							while True:
								user_input2 = input("Analyze> ")
								if user_input2 == "exit":
									print("Exiting Analyze Mode...")
									break
						if user_input == "exit":
							break
						elif user_input != "A":
							compare_Output = Compare_Model.GeminiVsGPT(user_input)
							print("If you want to analyze these output, type A")

				if user_input == "2":
					while True:
						print("GPT vs Llama: ")

						user_input = input("GPTvsLlama> ")
						if user_input == "A":
							Compare_Model.analyzeOutput(compare_Output)
							while True:
								user_input2 = input("Analyze> ")
								if user_input2 == "exit":
									print("Exiting Analyze Mode...")
									break
						if user_input == "exit":
							break
						elif user_input != "A":
							compare_Output = Compare_Model.GPTvsLlama(user_input)
							print("If you want to analyze these output, type A")

				if user_input == "3":
					while True:
						print("Gemini vs LLama: ")
						
						user_input = input("GeminiVsLlama> ")
						if user_input == "A":
							Compare_Model.analyzeOutput(compare_Output)
							while True:
								user_input2 = input("Analyze> ")
								if user_input2 == "exit":
									print("Exiting Analyze Mode...")
									break
						if user_input == "exit":
							break
						elif user_input != "A":
							compare_Output = Compare_Model.GeminiVsLlama(user_input)
							print("If you want to analyze these output, type A")
				

				


		elif command_line == "2":
			while True:
				print("Comparing All Models Mode: ")
				
				user_input = input("CompareAllModels> ")
				if user_input == "exit":
					break
				if user_input == "A":
					Compare_Model.analyzeOutput(compare_Output)
					while True:
						user_input2 = input("Analyze> ")
						if user_input2 == "exit":
							print("Exiting Analyze Mode...")
							break

				elif user_input != "A":
					compare_Output = Compare_Model.compareAll(user_input)
					print("If you want to analyze these output, type A")

			


		elif command_line == "exit":
			break   
