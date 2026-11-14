from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether, HRFlowable
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import HexColor
from xml.sax.saxutils import escape
import os

# output_path = ""

output_path = r""

doc = SimpleDocTemplate(output_path)
doc = SimpleDocTemplate(
    output_path,
    pagesize=A4,
    rightMargin=18*mm,
    leftMargin=18*mm,
    topMargin=18*mm,
    bottomMargin=17*mm,
    title="Machine Learning-Based Intrusion Detection System — 50 Interview Questions and Answers",
    author="OpenAI"
)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="CoverTitle", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=21, leading=26, textColor=HexColor("#16324F"),
    alignment=TA_CENTER, spaceAfter=10
))
styles.add(ParagraphStyle(
    name="SubtitleCustom", parent=styles["Normal"], fontSize=10.5, leading=15,
    textColor=HexColor("#526579"), alignment=TA_CENTER, spaceAfter=18
))
styles.add(ParagraphStyle(
    name="SectionCustom", parent=styles["Heading2"], fontName="Helvetica-Bold",
    fontSize=14, leading=18, textColor=HexColor("#16324F"),
    spaceBefore=13, spaceAfter=8, keepWithNext=True
))
styles.add(ParagraphStyle(
    name="QuestionCustom", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=9.5, leading=13, textColor=HexColor("#1D3557"),
    spaceBefore=7, spaceAfter=3, keepWithNext=True
))
styles.add(ParagraphStyle(
    name="AnswerCustom", parent=styles["BodyText"], fontSize=9.2, leading=13.2,
    textColor=HexColor("#263238"), spaceAfter=6
))
styles.add(ParagraphStyle(
    name="SmallCustom", parent=styles["BodyText"], fontSize=8.5, leading=12,
    textColor=HexColor("#455A64"), spaceAfter=5
))
styles.add(ParagraphStyle(
    name="CalloutCustom", parent=styles["BodyText"], fontSize=9, leading=13,
    textColor=HexColor("#263238"), leftIndent=8, rightIndent=8,
    borderColor=HexColor("#CBD5E1"), borderWidth=0.7, borderPadding=7,
    backColor=HexColor("#F4F7FA"), spaceBefore=5, spaceAfter=8
))

story = []
story.append(Spacer(1, 18*mm))
story.append(Paragraph("Machine Learning-Based<br/>Intrusion Detection System", styles["CoverTitle"]))
story.append(Paragraph("50 Project Interview Questions &amp; Answers", styles["SubtitleCustom"]))
story.append(HRFlowable(width="55%", thickness=1.2, color=HexColor("#3B6B8A"), hAlign="CENTER"))
story.append(Spacer(1, 12))
story.append(Paragraph(
    "<b>Preparation guide:</b> Beginner-to-advanced questions covering project fundamentals, "
    "dataset exploration, preprocessing, feature selection, machine learning algorithms, "
    "evaluation, and improvement ideas.",
    styles["CalloutCustom"]
))
story.append(Paragraph(
    "<b>Important scope note:</b> These answers describe the GFG-based implementation discussed "
    "in the conversation. Keep it separate from any other IDS internship project or implementation. "
    "Only claim steps, results, or deployment capabilities that you have personally implemented and verified.",
    styles["CalloutCustom"]
))
story.append(Spacer(1, 10))
story.append(Paragraph("Contents", styles["SectionCustom"]))
contents = [
    "1. Project fundamentals — Questions 1–10",
    "2. Dataset and exploratory data analysis — Questions 11–20",
    "3. Data preprocessing and feature engineering — Questions 21–35",
    "4. Machine learning algorithms — Questions 36–45",
    "5. Model evaluation and advanced concepts — Questions 46–50",
    "Whiteboard concepts and final preparation recommendations"
]
for item in contents:
    story.append(Paragraph("• " + escape(item), styles["AnswerCustom"]))
story.append(PageBreak())

sections = [
("1. Project fundamentals", [
("1. What is an Intrusion Detection System (IDS)?",
 "An IDS is a security system that monitors network traffic or system activities to identify suspicious behaviour, security violations, or potential attacks."),
("2. What problem does your project solve?",
 "It aims to identify malicious network activities and classify them into different attack categories using machine learning."),
("3. Why did you choose machine learning for intrusion detection?",
 "Machine learning can learn patterns from historical network traffic and use those patterns to classify new traffic records. It can help identify suspicious behaviour without relying only on predefined rules."),
("4. What is the difference between a traditional IDS and a machine-learning-based IDS?",
 "<b>Traditional IDS:</b> Uses predefined rules or known attack signatures.<br/><b>ML-based IDS:</b> Learns patterns from training data and predicts whether network activity belongs to particular categories."),
("5. What is the main objective of your project?",
 "To train and compare multiple machine learning classification algorithms and identify how effectively they classify network traffic into different attack categories."),
("6. What are the inputs and outputs of your system?",
 "<b>Input:</b> Network traffic features such as protocol type, service, connection duration, and byte counts.<br/><b>Output:</b> Predicted class or attack category."),
("7. Is your project supervised or unsupervised learning?",
 "It is supervised learning because the dataset contains labelled records. The model learns from network features along with their corresponding attack labels."),
("8. Is this classification or regression?",
 "It is a classification problem because the model predicts discrete categories, such as normal traffic or different attack types, rather than continuous numerical values."),
("9. What are the major stages in your project?",
 "Dataset exploration, preprocessing, feature selection, scaling, train-test splitting, model training, and evaluation."),
("10. What are the limitations of your project?",
 "The model depends on the quality and representativeness of its training dataset. It may struggle with previously unseen attacks, changing traffic patterns, and real-world network conditions. It also needs further testing before deployment in a live network.")
]),
("2. Dataset and exploratory data analysis", [
("11. Which dataset did you use, and why?",
 "The dataset used in the GFG implementation is the KDD Cup 1999 dataset (10% subset). It contains labelled network connection records with normal and attack activities, making it suitable for supervised intrusion detection experiments."),
("12. What does one row in your dataset represent?",
 "One row represents a network connection record containing different attributes that describe the connection, along with its corresponding label."),
("13. What are features and target variables?",
 "<b>Features (X):</b> Input attributes used by the model to make predictions.<br/><b>Target (y):</b> The output label that the model is expected to predict. For example, protocol type and source bytes are features, while attack type is the target."),
("14. What is the difference between numerical and categorical features?",
 "<b>Numerical:</b> Represent measurable quantities, such as duration and source bytes.<br/><b>Categorical:</b> Represent groups or labels, such as TCP, UDP, and ICMP."),
("15. What are protocol_type, service, and flag?",
 "<b>protocol_type:</b> Network protocol used, such as TCP, UDP, or ICMP.<br/><b>service:</b> Network service involved, such as HTTP or FTP.<br/><b>flag:</b> Connection status indicator describing the state of the connection."),
("16. What is the purpose of the dataset description file?",
 "The description file explains the dataset's features and their data types. It helps us understand which columns are numerical and which are categorical."),
("17. What is EDA?",
 "Exploratory Data Analysis is the process of understanding a dataset through its structure, distributions, data types, missing values, and visualizations before building a model."),
("18. How did you identify categorical columns?",
 "I identified numerical columns using Pandas' _get_numeric_data() method. Then I used set difference to identify non-numerical columns and excluded the target columns."),
("19. Why did you visualize categorical feature distributions?",
 "To understand how frequently different categories occur in the dataset. For example, visualizing protocol types helps us understand the distribution of TCP, UDP, and ICMP records."),
("20. What is the difference between normal traffic and attack traffic?",
 "Normal traffic represents legitimate network communication, whereas attack traffic represents connections associated with malicious or suspicious activities.")
]),
("3. Data preprocessing and feature engineering", [
("21. Why is data preprocessing necessary?",
 "Raw data may contain missing values, categorical values, inconsistent formats, or irrelevant features. Preprocessing prepares the data in a suitable format for machine learning algorithms."),
("22. How did you handle missing values?",
 "The implementation uses dropna(axis='columns') to remove columns containing missing values."),
("23. What does dropna(axis='columns') do?",
 "It removes entire columns that contain at least one missing value. axis=0 removes rows; axis=1 removes columns."),
("24. What is categorical encoding?",
 "Categorical encoding converts text-based categories into numerical representations so machine learning algorithms can process them."),
("25. Why did you convert categorical values into integers?",
 "Many machine learning algorithms require numerical input. Therefore, I mapped categorical values such as TCP, UDP, and ICMP to numerical values."),
("26. What is the purpose of train_test_split()?",
 "It divides the dataset into training and testing subsets. The training data is used to train the model, while the testing data is used to evaluate its performance on unseen records."),
("27. Why did you use test_size=0.33?",
 "It allocates 33% of the dataset for testing and the remaining 67% for training."),
("28. What is the purpose of random_state=42?",
 "It ensures reproducibility. The same random seed produces the same train-test split when the code is executed again."),
("29. What is correlation analysis?",
 "Correlation analysis measures the relationship between numerical features. Values generally range from -1 to +1: +1 indicates strong positive correlation, -1 strong negative correlation, and 0 no linear correlation."),
("30. Why did you remove highly correlated features?",
 "Highly correlated features may contain redundant information. Removing selected redundant features can reduce dimensionality and potentially improve model efficiency."),
("31. What is feature selection?",
 "Feature selection is the process of selecting useful input features and removing irrelevant or redundant ones to simplify the model."),
("32. Why did you remove the service column?",
 "The implementation removes it as part of its feature-selection process to reduce the number of input features. However, service information may be useful for detecting attacks, so its removal should ideally be validated by comparing model performance with and without it."),
("33. What is MinMaxScaler, and why did you use it?",
 "MinMaxScaler is a feature-scaling technique that transforms numerical values into a specified range, usually 0 to 1. It helps prevent features with larger numerical ranges from dominating algorithms that are sensitive to feature scale."),
("34. What is the difference between fit_transform() and transform()?",
 "<b>fit_transform():</b> Learns the scaling parameters from the training data and transforms it.<br/><b>transform():</b> Applies the already learned parameters to other data, such as testing data. We fit only on training data to avoid data leakage."),
("35. What is data leakage, and how did you avoid it?",
 "Data leakage occurs when information from the testing data influences the training process, leading to overly optimistic evaluation results. I used the training data to fit the scaler and applied the same transformation to the testing data.")
]),
("4. Machine learning algorithms", [
("36. Which six machine learning algorithms did you implement?",
 "Naive Bayes, Decision Tree, Random Forest, Support Vector Machine (SVM), Logistic Regression, and Gradient Boosting."),
("37. How does Naive Bayes work?",
 "Naive Bayes is a probabilistic classification algorithm based on Bayes' theorem. It predicts a class by calculating its probability based on the input features, assuming the features are conditionally independent given the class."),
("38. How does a Decision Tree make predictions?",
 "A Decision Tree makes predictions by splitting data based on feature conditions. It follows a series of decision rules from the root node to a leaf node, which provides the final predicted class."),
("39. What is the difference between Gini impurity and entropy?",
 "Both measure the quality of a split in a Decision Tree. Gini impurity measures the chance of incorrect classification if a sample is randomly labelled according to the class distribution. Entropy measures impurity or uncertainty. Lower values indicate purer groups."),
("40. What is Random Forest, and how is it different from a Decision Tree?",
 "A Decision Tree uses one tree to make predictions. Random Forest combines predictions from multiple decision trees to improve stability and reduce overfitting. This implementation uses 30 trees through n_estimators=30."),
("41. What is SVM, and what is the purpose of its kernel?",
 "Support Vector Machine finds a decision boundary that separates classes. A kernel helps SVM handle non-linear relationships by implicitly representing data in a higher-dimensional feature space."),
("42. What is Logistic Regression, and why is it used for classification?",
 "Logistic Regression is a classification algorithm that estimates the probability of a class using a logistic function. It can be extended to multiclass classification."),
("43. What is Gradient Boosting?",
 "Gradient Boosting is an ensemble learning technique that builds models sequentially. Each new model tries to correct the errors made by the previous models."),
("44. What is the difference between bagging and boosting?",
 "<b>Bagging:</b> Models are trained independently, often in parallel, and it can reduce variance. Random Forest is an example.<br/><b>Boosting:</b> Models are trained sequentially, with later models focusing on previous errors. Gradient Boosting is an example."),
("45. Why did you compare multiple algorithms instead of using only one?",
 "Different algorithms learn patterns differently. Comparing multiple algorithms helps identify which one provides the best balance of classification performance and computational efficiency for the dataset.")
]),
("5. Model evaluation and advanced concepts", [
("46. What is the difference between training accuracy and testing accuracy?",
 "<b>Training accuracy:</b> Measures how accurately the model predicts records it was trained on.<br/><b>Testing accuracy:</b> Measures how accurately it predicts unseen records. Testing accuracy gives a better indication of generalisation."),
("47. What are accuracy, precision, recall, and F1-score?",
 "<b>Accuracy:</b> Overall proportion of correct predictions.<br/><b>Precision:</b> Of the records predicted as a particular class, how many were actually that class?<br/><b>Recall:</b> Of the actual records belonging to a class, how many did the model correctly identify?<br/><b>F1-score:</b> Harmonic mean of precision and recall. For intrusion detection, recall is especially important because low recall can mean actual attacks are missed."),
("48. What is a confusion matrix?",
 "A confusion matrix compares actual labels with predicted labels. For binary classification, it contains True Positive (TP), True Negative (TN), False Positive (FP), and False Negative (FN). In intrusion detection, a false negative can mean an actual attack was incorrectly classified as normal traffic."),
("49. What are overfitting and underfitting?",
 "<b>Overfitting:</b> The model performs very well on training data but poorly on unseen testing data.<br/><b>Underfitting:</b> The model fails to learn the underlying patterns and performs poorly on both training and testing data."),
("50. How would you improve the performance of your intrusion detection system?",
 "I would explore better feature selection, tune hyperparameters using cross-validation, evaluate class imbalance, and experiment with more suitable encoding techniques. I would also test the model on newer and more diverse network traffic datasets to improve its ability to generalise.")
])
]

for section_title, qa_list in sections:
    story.append(Paragraph(section_title, styles["SectionCustom"]))
    for q, a in qa_list:
        story.append(KeepTogether([
            Paragraph(escape(q), styles["QuestionCustom"]),
            Paragraph(a, styles["AnswerCustom"])
        ]))

story.append(PageBreak())
story.append(Paragraph("Whiteboard concepts to know", styles["SectionCustom"]))
story.append(Paragraph("<b>1. Train-test split</b>", styles["QuestionCustom"]))
story.append(Paragraph(
    "The discussed split is 67% training data and 33% testing data. Training data teaches the model; testing data evaluates it on records held out from training.",
    styles["AnswerCustom"]))
story.append(Paragraph("<b>2. Feature scaling</b>", styles["QuestionCustom"]))
story.append(Paragraph(
    "MinMaxScaler uses: <b>X' = (X − X_min) / (X_max − X_min)</b>. The minimum and maximum are learned from the training set and reused for the test set.",
    styles["AnswerCustom"]))
story.append(Paragraph("<b>3. Decision Tree vs Random Forest</b>", styles["QuestionCustom"]))
story.append(Paragraph(
    "A Decision Tree makes predictions using one tree. Random Forest combines predictions from many trees.",
    styles["AnswerCustom"]))
story.append(Paragraph("<b>4. Precision vs Recall</b>", styles["QuestionCustom"]))
story.append(Paragraph(
    "Precision focuses on avoiding false alarms among predicted attacks. Recall focuses on detecting actual attacks and avoiding missed attacks.",
    styles["AnswerCustom"]))
story.append(Paragraph("<b>5. Overfitting vs Underfitting</b>", styles["QuestionCustom"]))
story.append(Paragraph(
    "Overfitting means the model learns the training data too closely and generalises poorly. Underfitting means it has not learned the underlying patterns well enough.",
    styles["AnswerCustom"]))

story.append(Paragraph("Important implementation notes", styles["SectionCustom"]))
notes = [
    "<b>Dataset:</b> The GFG implementation discussed here uses the KDD Cup 1999 dataset (10% subset). Verify the exact files and labels in the notebook you run.",
    "<b>Encoding:</b> The manual category-to-integer mapping is not one-hot encoding.",
    "<b>Service feature:</b> The shown implementation drops the service column; do not say it was encoded.",
    "<b>Split:</b> The discussed code uses a 67:33 train-test split, rather than loading a separate pre-existing test dataset.",
    "<b>Metrics:</b> In single-label multiclass classification, weighted recall equals accuracy. Macro recall is more informative when comparing performance across attack categories.",
    "<b>Claims:</b> Do not quote a winning algorithm or accuracy percentage until you have run the code and verified the results. Do not claim live packet capture or live-network monitoring unless you built those capabilities."
]
for n in notes:
    story.append(Paragraph("• " + n, styles["AnswerCustom"]))

story.append(Paragraph("Final preparation recommendations", styles["SectionCustom"]))
story.append(Paragraph(
    "Start with Questions 1–35 and understand the complete data pipeline. Then prepare the six algorithms and evaluation metrics. Be ready to explain each code section, why it is used, and what would happen if that step were changed.",
    styles["CalloutCustom"]))
story.append(Paragraph(
    "The most important areas to prepare first are: project objective and workflow; dataset features and labels; train-test split; categorical encoding; correlation and feature selection; MinMaxScaler; the differences between the six algorithms; and accuracy, precision, recall, F1-score, and confusion matrix.",
    styles["AnswerCustom"]))
story.append(Paragraph(
    "<b>Interview strategy:</b> Explain the implementation you actually built and tested. If you discuss a possible improvement that is not in the original code, clearly present it as an improvement you would make, not as something already implemented.",
    styles["CalloutCustom"]))

def add_page_number(canvas, doc):
    canvas.saveState()
    page_num = canvas.getPageNumber()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(HexColor("#607080"))
    canvas.drawString(18*mm, 9*mm, "ML-Based Intrusion Detection System | Interview Preparation")
    canvas.drawRightString(A4[0] - 18*mm, 9*mm, f"Page {page_num}")
    canvas.restoreState()

doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)

print(f"Created PDF: {output_path}")
