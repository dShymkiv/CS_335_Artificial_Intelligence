{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMekdreJySOERNFHg2VDbPB",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/dShymkiv/CS_335_Artificial_Intelligence/blob/main/CS335_PythonLab1_DianaShymkiv.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LVyZ5MSa0MPi",
        "outputId": "47b8835e-815e-4789-b132-a723061f7b1a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Name: Diana Shymkiv\n",
            "Age in 5 years: 26\n",
            "Is enrolled in CS 335 course? True\n"
          ]
        }
      ],
      "source": [
        "name = \"Diana Shymkiv\"\n",
        "age = 21\n",
        "ai_course = True\n",
        "\n",
        "print(\"Name:\", name)\n",
        "print(\"Age in 5 years:\", age + 5)\n",
        "print(\"Is enrolled in CS 335 course?\", ai_course)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "topics = [\"Logic\", \"Search\", \"NLP\", \"ML\", \"Bayesian Inference\", \"Neural Networks\", \"Computer Vision\"]\n",
        "\n",
        "# for topic in topics:\n",
        "#   print(\"We will study:\", topic)\n",
        "\n",
        "for i, topic in enumerate(topics, start=1):\n",
        "  print( \"We will study:\", f\"{i}. {topic}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V3_9YdSX0xIF",
        "outputId": "e055cf3a-0220-4e0e-c670-8bd7b744fae5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "We will study: 1. Logic\n",
            "We will study: 2. Search\n",
            "We will study: 3. NLP\n",
            "We will study: 4. ML\n",
            "We will study: 5. Bayesian Inference\n",
            "We will study: 6. Neural Networks\n",
            "We will study: 7. Computer Vision\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "student = {\"name\": \"Diana\", \"score\": 94}\n",
        "\n",
        "if student[\"score\"] >= 95:\n",
        " grade = \"A+\"\n",
        "elif student[\"score\"] >= 90:\n",
        " grade = \"A\"\n",
        "elif student[\"score\"] >= 80:\n",
        " grade = \"B\"\n",
        "else:\n",
        " grade = \"C or below\"\n",
        "\n",
        "print(f\"{student['name']} received a grade of {grade}.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Gnj-8oyf1g1X",
        "outputId": "b492b8ed-b252-4d67-926b-7368e1a60377"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Diana received a grade of A.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def greet_student(name):\n",
        "  return f\"Welcome to Omeed, {name}!\"\n",
        "\n",
        "# Test\n",
        "print(greet_student(\"Diana\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "A7QxLLhX2fuu",
        "outputId": "a7cd2e45-77f4-4afb-cee7-a82bf9ad2e09"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Welcome to Omeed, Diana!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def square_number(num):\n",
        "    return num ** 2\n",
        "\n",
        "# Test\n",
        "print(square_number(2))\n",
        "print(square_number(-9))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UouztyRQ26ZO",
        "outputId": "e82a6d6a-ac38-4b46-ed66-016bd38bf171"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4\n",
            "81\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "OnbXlE9O3SnX"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}