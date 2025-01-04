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
		geminiOutput = Gemini_Model.output("analyze these answer of each model " + user_input)
		geminiOutput2 = Gemini_Model.output("Only list the answers chosen by each model (without any explanations) in the format Model Name: A,B,C,D. Analyze the answers of each model." + user_input)