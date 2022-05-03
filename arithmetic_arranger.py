def arithmetic_arranger(problems, calculate = False):
    
  #Assert that there are less than 5 problems
  num_problems = len(problems)
  if num_problems > 5: return "Error: Too many problems."

  #Help variables  
  pad = "    "
  arranged_problems = ""
  operation_data = []
  #----------------------------------------------------Start----------------------------------------------------
  #------------------------------------Error Checking and Data Aquisition---------------------------------------
  
  #Divide each problem into 2 operands and 1 operator
  for problem in problems:
    #Dictionary to save data of the problem
    operation_dict = {}
    div_problem = problem.split()
    #Assert that there are 3 values in the list
    if len(div_problem) != 3: return "Error: Bad formatting."
    #Save the string values of the operands
    operation_dict["operands"] = [div_problem[0],div_problem[2]]
    #Assert that the operand is '+' or '-'

    if (div_problem[1] != '+') and (div_problem[1] !='-'): return "Error: Operator must be '+' or '-'."
    operation_dict["operator"] = div_problem[1]
    #Assert that the operands are 
    try:
    #Assert that the input are numbers and output the result
      if operation_dict["operator"] == '+': operation_dict["result"] = str(int(div_problem[0]) + int(div_problem[2]))
      else: operation_dict["result"] = str(int(div_problem[0]) - int(div_problem[2]))
    except:
      return "Error: Numbers must only contain digits."
    
    #Assert that the number is equal or less than 4
    if (len(div_problem[0]) > 4) or (len(div_problem[2]) > 4): return "Error: Numbers cannot be more than four digits."
    #Store the length of the longest operand in a variable 
    operation_dict["width"] = [len(div_problem[0]),len(div_problem[2])]
    operation_dict["max width num"] = max(operation_dict["width"])
    operation_dict["operation width"] = operation_dict["max width num"] + 2
    #Create a list of the dictionaries
    operation_data.append(operation_dict)

  #-----DEBUG---------#
  #print(operation_data)
  #-----DEBUG---------#

  #-------------------------------------Error Checking and Data Aquisition-------------------------------------
  #----------------------------------------------------End-----------------------------------------------------

  #----------------------------------------------------Start---------------------------------------------------
  #---------------------------------------------Output Formatting----------------------------------------------

  #Formatting of each problem
  block_formats = []
  
  for problem in range(num_problems):
    format_dict = {}
    
    format_dict["row 0"] = " " * (operation_data[problem]["operation width"] - operation_data[problem]["width"][0]) + operation_data[problem]["operands"][0]
    format_dict["row 1"] = operation_data[problem]["operator"] + " " * (operation_data[problem]["operation width"] - operation_data[problem]["width"][1] - 1) + operation_data[problem]["operands"][1]
    format_dict["row 2"] = "-" * operation_data[problem]["operation width"]
    if calculate: format_dict["row 3"] = " " * (operation_data[problem]["operation width"] - len(operation_data[problem]["result"])) + operation_data[problem]["result"]

    block_formats.append(format_dict)

  #Formatting output
  if calculate: rows = 4
  else: rows = 3

  for row in range(rows):
    for problem in range(num_problems):
      separate = ""
      if problem < num_problems-1: separate = pad
      elif row < rows-1: separate = "\n"
      
      
      arranged_problems += block_formats[problem]["row " + str(row)] + separate
  
  #---------------------------------------------Output Formatting----------------------------------------------
  #----------------------------------------------------End-----------------------------------------------------
  return arranged_problems

print(arithmetic_arranger(['3801 - 2', '123 + 49'], False))
