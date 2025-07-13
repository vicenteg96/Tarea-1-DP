import matplotlib.pyplot as plt

def plot_f1_scores(df_eval):
    #Funcion que grafica el F1-score mensual del modelo.
    
    plt.figure(figsize=(8, 4))
    plt.plot(df_eval['mes'], df_eval['f1_score'], marker='o', linestyle='-', label="F1-score")
    plt.title("F1-score mensual del modelo")
    plt.xlabel("Mes")
    plt.ylabel("F1-score")
    plt.ylim(0, 1)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_class_distribution(df_eval):
    #Funcion que grafica la distribucion de clases por mes.
    
    plt.figure(figsize=(8, 4))
    plt.plot(df_eval['mes'], df_eval['pct_high_tip'], marker='o', label='% High Tip')
    plt.plot(df_eval['mes'], df_eval['pct_low_tip'], marker='o', label='% Low Tip')
    plt.title("Distribución de clases por mes")
    plt.xlabel("Mes")
    plt.ylabel("Proporción")
    plt.ylim(0, 1)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
