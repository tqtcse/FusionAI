from gemini import Gemini_Model
from llama import Llama_Model
from gpt import GPT_Model



class Compare_Model:
	def GeminiVsLlama(user_input):
		print("Gemini Model: ")
		geminiOutput = Gemini_Model.output(user_input)
		print("Llama Model: ")
		llamaOutput = Llama_Model.output(user_input)

		output = "Gemini: " + geminiOutput + "Llama: " + llamaOutput
		return output

	def GeminiVsGPT(user_input):
		print("Gemini Model: ")
		geminiOutput = Gemini_Model.output(user_input)
		print("GPT Model: ")
		gptOutput = GPT_Model.output(user_input)
		output = "Gemini: " + geminiOutput + "GPT: " + gptOutput
		return output

	def GPTVsLlama(user_input):
		print("GPT_Model: ")
		gptOutput = GPT_Model.output(user_input)
		print("Llama Model: ")
		llamaOutput = Llama_Model.output(user_input)
		output = "Llama Model: " + llamaOutput + "GPT: " + gptOutput
		return output

	def compareAll(user_input):
		print("Gemini Model: ")
		geminiOutput = Gemini_Model.output(user_input)
		print("Llama Model: ")
		llamaOutput = Llama_Model.output(user_input)
		print("GPT Model: ")
		gptOutput = GPT_Model.output(user_input)

		output = "Gemini: " + geminiOutput + "Llama: " + llamaOutput + "GPT: " + gptOutput
		return output 
		
	def analyzeOutput(user_input):
		#geminiAnalyze
		# geminiOutput = Gemini_Model.output("analyze these answer of each model " + user_input)
		geminiOutput2 = Gemini_Model.output("Only list the answers chosen by each model (without any explanations) in the format Model Name: A,B,C,D." + user_input)

		geminiOutput2 = geminiOutput2.splitlines()
		# geminiOutput2 = [" ".join(geminiOutput2[i:i+2]) for i in range(0, len(geminiOutput2), 2)]

		answers = [resp.split(": ")[1] for resp in geminiOutput2]
		counts = {key: 0 for key in "ABCD"}
		for answer in answers:
			if answer in counts:
				counts[answer] += 1
		total_responses = len(answers)
		percentages = {key: (counts[key] / total_responses) * 100 for key in counts}
		# In kết quả
		for key in percentages:
			print(f"{key}: {percentages[key]:.0f}%")
