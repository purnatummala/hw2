# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u


# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------


def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}

    level1["smoking"] = 1.0
    level1["smoking_info_gain"] = 0.2780719051126377

    level1["cough"] = -1
    level1["cough_info_gain"] = 0.034851554559677034

    level1["radon"] = -1
    level1["radon_info_gain"] = 0.2364527976600279

    level1["weight_loss"] = -1
    level1["weight_loss_info_gain"] = 0.02904940554533142

    level2_left["smoking"] = -1
    level2_left["smoking_info_gain"] = 0

    level2_right["smoking"] = -1
    level2_right["smoking_info_gain"] = 0

    level2_left["radon"] = -1
    level2_left["radon_info_gain"] = 0

    level2_left["cough"] = 1.0
    level2_left["cough_info_gain"] = 0.7219280948873623

    level2_left["weight_loss"] = -1
    level2_left["weight_loss_info_gain"] = -1

    level2_right["radon"] = 1.0
    level2_right["radon_info_gain"] = 0.7219280948873623

    level2_right["cough"] = -1
    level2_right["cough_info_gain"] = -1

    level2_right["weight_loss"] = -1
    level2_right["weight_loss_info_gain"] = -1

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    # Fill up `construct_tree``
    # tree, training_error = construct_tree() 
        
    tree = u.BinaryTree('Smoking Tobacco')

    cough = tree.insert_left('Chronic Cough')
    radon = tree.insert_left('Radon Exposure')

    cough.insert_right(1)
    cough.insert_left(4)

    radon.insert_left(1)
    radon.insert_right(4)
    answer["tree"] = tree  
    answer["training_error"] = 0.0  




    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}

    answer["(a) entropy_entire_data"] = 1.4253642047367425

    answer["(b) x <= 0.2"] = 0.17739286055515824
    answer["(b) x <= 0.7"] = 0.3557029418697566
    answer["(b) y <= 0.6"] = 0.34781842724338197

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = "y=0.6"  

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("y <= 0.6")
    left = tree.insert_left("x <= 0.7")
    right = tree.insert_right("x <= 0.2")

    left.insert_left("B")
    
    y_03 = left.insert_right("y <= 0.3")
    y_03.insert_left("A")
    y_03.insert_right("C")

    right.insert_right("A")
    y_08 = right.insert_left("y <= 0.8")
    y_08.insert_right("B")
    y_08.insert_left("C")

    answer["(d) full decision tree"] = tree

    return answer

# ----------------------------------------------------------------------


def question3():
    answer = {}

    # float
    answer["(a) Gini, overall"] = 0.5

    # float
    answer["(b) Gini, ID"] = 0.0
    answer["(c) Gini, Gender"] = 0.48
    answer["(d) Gini, Car type"] = 0.1625
    answer["(e) Gini, Shirt type"] = 0.4914405

    answer["(f) attr for splitting"] = "Car Type"

    # Explanatory text string
    answer["(f) explain choice"] = "Car type has the lowest Gini index of all, excluding ID. ID is an identification column and cannot be treated for the Gini index, as it holds no value in that context. With a lower Gini index, Car Type is a purer class than Shirt Size, and so is a better attribute to split on."
    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # Classifications for various types of data
    continuous = 'continuous'
    discrete = 'discrete'
    binary = 'binary'
    qualitative = 'qualitative'
    quantitative = 'quantitative'
    nominal = 'nominal'
    ordinal = 'ordinal'
    interval = 'interval'
    ratio = 'ratio'

    # Paraphrased explanations
    continuous_exp = 'Measures that can be infinitely divided, offering an unending scale of values.'
    quantitative_exp = 'The importance of the data lies in its numerical representation.'
    ratio_exp = 'The presence of an absolute zero allows for meaningful comparisons and calculations.'
    
    # Assignments and explanations
    answer["a"] = [continuous, quantitative, ratio]
    answer["a: explain"] = "This classification is due to the ability to divide measures indefinitely, emphasizing the numerical importance and the existence of an absolute zero point which cannot be surpassed, symbolizing a fundamental starting point."

    answer["b"] = [discrete, quantitative, ratio]
    answer["b: explain"] = "The nature of being countable with distinct gaps between values, alongside the significance of numerical representation and the existence of an absolute zero, highlights the absence of light as a definitive lower limit."

    answer["c"] = [discrete, qualitative, ordinal]
    answer["c: explain"] = "Given the finite descriptive categories for light levels, the assessment relies on subjective judgment ranked in a specific order from dim to bright."

    answer["d"] = [continuous, quantitative, ratio]
    answer["d: explain"] = "The divisibility of measurements into finer scales, the reliance on numeric value, and a zero point indicating an absence of angle, support continuous, quantitative, and ratio classifications respectively."

    answer["e"] = [discrete, qualitative, ordinal]
    answer["e: explain"] = "The limitation to three distinct levels, identification through titles, and a hierarchical arrangement underscore the discrete, qualitative, and ordinal nature of this data."

    answer["f"] = [continuous, quantitative, interval]
    answer["f: explain"] = continuous_exp + quantitative_exp + "An interval classification is due to the lack of an absolute zero, allowing for negative values, similar to temperatures below zero."

    answer["g"] = [discrete, quantitative, ratio]
    answer["g: explain"] = "The enumeration of patients, their numeric value, and the presence of an absolute zero (eliminating negative counts) dictate these classifications."

    answer["h"] = [discrete, qualitative, nominal]
    answer["h: explain"] = "ISBNs, being indivisible identifiers and used purely for identification without a numeric value or order, fall into discrete, qualitative, and nominal categories."

    answer["i"] = [discrete, qualitative, ordinal]
    answer["i: explain"] = "Limited levels of translucency, judged rather than measured numerically, and ranked from opaque to translucent, classify this data as discrete, qualitative, and ordinal."

    answer["j"] = [discrete, qualitative, ordinal]
    answer["j: explain"] = "The fixed number of ranks, their designation by title, and their hierarchical organization categorize military ranks as discrete, qualitative, and ordinal."

    answer["k"] = [continuous, quantitative, ratio]
    answer["k: explain"] = continuous_exp + quantitative_exp + ratio_exp + "Center proximity, measured without subdivisions, emphasizes a fundamental starting or zero point."

    answer["l"] = [continuous, quantitative, ratio]
    answer["l: explain"] = continuous_exp + quantitative_exp + ratio_exp + "Though theoretical, the concept of zero density represents an absolute baseline, underscoring the possibility of measuring emptiness."

    answer["m"] = [discrete, qualitative, nominal]
    answer["m: explain"] = "Coat check numbers, serving as unique identifiers without division or numeric comparison, illustrate discrete, qualitative, and nominal traits."

    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Reinterpreted explanations for the choice between two models based on their performance and approach to handling data

    explain["a"] = "Model 2"
    explain["a explain"] = "Opting for Model 2 due to its superior performance on test data, indicating better generalization capabilities. Model 1 demonstrates a tendency towards overfitting, evident from its significantly higher training accuracy compared to its test accuracy, suggesting it may not perform as well on new, unseen data."

    explain["b"] = "Model 2"
    explain["b explain"] = "Choosing Model 2 again, based on its overall higher performance metrics across both datasets. Despite both models being trained on Dataset A and achieving high accuracy, Model 2 outperforms on Dataset B, which serves as a more critical test of the model's ability to handle unseen data effectively."

    explain["c similarity"] = "Model Complexity Consideration"
    explain["c similarity explain"] = "Both methodologies, MDL and pessimistic error estimation, are strategies that introduce penalties for overly complex decision trees. Their goal is to strike a balance between fitting the training data well and maintaining a manageable model size or complexity, with the premise that simpler models tend to generalize better."

    explain["c difference"] = "Handling of Model Complexity"
    explain["c difference explain"] = "The MDL Principle balances model fit against complexity by considering the succinctness of the model's description as a measure of complexity. Conversely, the pessimistic error estimate adjusts the tree's error estimate by incorporating a complexity penalty, which correlates with the tree's intricacy, such as the number of terminal nodes."

    return explain



# ----------------------------------------------------------------------
def question6():
    answer = {}
    # Decision tree rules based on the split criteria
    answer["a, level 1"] = "x <= 0.8"
    answer["a, level 2, left"] = "y <= 0.6"
    answer["a, level 2, right"] = "A"  # Everything to the right of x=0.8 is class A
    answer["a, level 3, left"] = "B"   # The bottom left square (0.2*0.4) area is class B
    answer["a, level 3, right"] = "A"  # The rest above the y=0.6 line is class A

    # Calculate the expected error rate based on misclassified areas
    # The misclassified area for class B is the top left corner, not covered by the decision tree
    # Therefore, the error is the area of B not covered by the tree (0.2 * 0.4)
    # The area of B is 0.2 width * 0.4 height = 0.08
    # The total area is 1, so the expected error rate is the area of B divided by the total area
    misclassified_area = 0.08
    total_area = 1
    answer["b, expected error"] = misclassified_area / total_area

    # Define the binary tree using the provided u.BinaryTree class and the nodes created above
    tree = u.BinaryTree("x <= 0.8")
    left_node = tree.insert_left("y <= 0.6")
    right_node = tree.insert_right("A")
    left_node.insert_left("B")
    left_node.insert_right("A")

    answer["c, tree"] = tree
    return answer



# ----------------------------------------------------------------------
def question7():
    answer = {}

    # float
    answer["a, info gain, ID"] = 1.0
    answer["b, info gain, Handedness"] = 0.5310044

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "Handedness"

    # answer is a float
    answer["d, gain ratio, ID"] = 0.23137821315975915
    answer["e, gain ratio, Handedness"] = 0.531

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = "Handedness"

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)

