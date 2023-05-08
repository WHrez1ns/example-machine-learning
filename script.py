# Documentação de exemplo: https://code.tutsplus.com/pt/tutorials/introduction-to-machine-learning-in-python--cms-30623
# Código alterado por Fábio Henrique Cabrini
# Maio de 2023

# Instalar o sklearn
# pip install scikit-learn

from sklearn import tree  # importa o módulo "tree" do Sklearn Árvore de Decisão
features = [[7, 0.6, 40], [7, 0.6, 41], [6, 0.4, 42], [7, 0.6, 35],
            [32, 600, 37], [33, 620, 38], [38, 615, 35], [35, 550, 34]]
# labels = [galinha, galinha, cavalo, cavalo]
# Uma galinha será representada por 0, enquanto um cavalo será representado por 1
labels = [0, 0, 0, 0, 1, 1, 1, 1]  # número de classes
classif = tree.DecisionTreeClassifier()  # Classificador
classif.fit(features, labels)
altura = float(input("Digite a altura do animal: "))
peso = float(input("Digite a o peso do animal: "))
temperatura = float(input("Digite a temperatura do animal: "))
x = classif.predict([[altura, peso, temperatura]])
if x == 0:
    print("O animal é uma Galinha!")
else:
    print("O animal é um Cavalo!")
