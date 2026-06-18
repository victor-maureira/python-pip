import matplotlib.pyplot as plt


def generate_barchart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig("bar.png")
    plt.close()


def generate_pychart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis("equal")
    plt.savefig("pie.png")
    plt.close()


if __name__ == "__main__":
    labels = ["Chile", "Brazil", "Colombia"]
    values = [19000, 22400, 30340]
    # generate_barchart(labels, values)
    generate_pychart(labels, values)
