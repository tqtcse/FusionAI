from gemini import Gemini_Model
from llama import Llama_Model

class Compare_Model:
	def GeminiVsLlama(user_input):
		geminiOutput = Gemini_Model.output(user_input)
		llamaOutput = Llama_Model.output(user_input)
		print("Gemini Model: ", geminiOutput)
		print("Llama Model: ", llamaOutput)