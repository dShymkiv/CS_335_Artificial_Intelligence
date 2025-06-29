{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMn7n9k8XcH3MQoLpUKxm29",
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
        "<a href=\"https://colab.research.google.com/github/dShymkiv/CS_335_Artificial_Intelligence/blob/main/sentiment_analyzer.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 653
        },
        "id": "OTGeXGW0bgfE",
        "outputId": "30a6aac0-1c25-4543-fcb9-8437e5047d27"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Positive Lexicon: ['amazing', 'awesome', 'bliss', 'brilliant', 'delight', 'ecstatic', 'excellent', 'fantastic', 'great', 'happy', 'joy', 'love', 'outstanding', 'perfect', 'pleasure', 'superb', 'terrific', 'wonderful']\n",
            "Negative Lexicon: ['angry', 'anxious', 'awful', 'bad', 'depress', 'disappoint', 'disaster', 'failure', 'fear', 'hate', 'horrible', 'miserable', 'pain', 'sad', 'scared', 'terrible', 'ugly', 'worst']\n",
            "\n",
            "Enter sentences to analyze sentiment (type 'exit' to quit):\n",
            "> he is sad and happy\n",
            "Tokens: ['he', 'is', 'sad', 'and', 'happy']\n",
            "+ matches: 1, - matches: 1\n",
            "Score: 0.000 => Neutral\n",
            "\n",
            "> he is sad\n",
            "Tokens: ['he', 'is', 'sad']\n",
            "+ matches: 0, - matches: 1\n",
            "Score: -0.333 => Negative\n",
            "\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "Interrupted by user",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipython-input-4-1363850028.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"\\nEnter sentences to analyze sentiment (type 'exit' to quit):\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m     \u001b[0mtext\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'> '\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstrip\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mtext\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlower\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32min\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0;34m'exit'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'quit'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m         \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Goodbye!\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m   1175\u001b[0m                 \u001b[0;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1176\u001b[0m             )\n\u001b[0;32m-> 1177\u001b[0;31m         return self._input_request(\n\u001b[0m\u001b[1;32m   1178\u001b[0m             \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mprompt\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1179\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"shell\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m   1217\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1218\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1219\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Interrupted by user\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1220\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1221\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Invalid Message:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
          ]
        }
      ],
      "source": [
        "\"\"\"\n",
        "Assignment 5: Simple Sentiment Analyzer\n",
        "\n",
        "Instructions:\n",
        "1. Modify the `positive_words` and `negative_words` sets below:\n",
        "   - **Add at least 15 positive words** and **15 negative words** of your choice.\n",
        "   - Ensure words are lowercased and contain only alphabetic characters.\n",
        "2. Print positive lexicon & negative lexicon\n",
        "3. Compute simple sentiment score (hint: positive - negative count)\n",
        "4. Print the output results\n",
        "5. Add a short reflection as comments at the bottom:\n",
        "   - Discuss **strengths** and **limitations** of this lexicon-based approach (2–3 sentences).\n",
        "\n",
        "Deliverables:\n",
        "- Completed Python script (`sentiment_analyzer.py`).\n",
        "\n",
        "\"\"\"\n",
        "\n",
        "# --- Grading Rubric (Total: 60 pts) ---\n",
        "#\n",
        "# | Criteria                                                          | Points |\n",
        "# |:------------------------------------------------------------------|:-------|\n",
        "# | Lexicon completeness (≥15 positive & ≥15 negative words)           |   20   |\n",
        "# | Display of positive & negative lexicons                            |    5   |\n",
        "# | Sentiment score computation & correct labeling                    |   15   |\n",
        "# | Interactive testing functionality (I/O loop, 'exit' handling)     |   10   |\n",
        "# | Code readability and comments                                     |    5   |\n",
        "# | Reflection quality (insightful strengths & limitations)          |    5   |\n",
        "#\n",
        "# **Total Points:** 60\n",
        "\n",
        "import re\n",
        "\n",
        "def clean_text(text):\n",
        "    \"\"\"\n",
        "    Lowercase, remove punctuation, and split into tokens.\n",
        "    \"\"\"\n",
        "    text = text.lower()\n",
        "    text = re.sub(r\"[^a-z\\s]\", '', text)\n",
        "    tokens = text.split()\n",
        "    return tokens\n",
        "\n",
        "# 1. Add 15 positive and 15 negative to your expand the knowledge base\n",
        "\n",
        "positive_words = {\n",
        "    'happy', 'joy', 'love', 'excellent', 'awesome', 'fantastic', 'amazing',\n",
        "    'wonderful', 'great', 'perfect', 'superb', 'brilliant', 'delight',\n",
        "    'pleasure', 'ecstatic', 'bliss', 'outstanding', 'terrific'\n",
        "}\n",
        "\n",
        "negative_words = {\n",
        "    'sad', 'angry', 'hate', 'terrible', 'awful', 'horrible', 'bad',\n",
        "    'worst', 'pain', 'disappoint', 'ugly', 'fear', 'scared', 'anxious',\n",
        "    'depress', 'miserable', 'failure', 'disaster'\n",
        "}\n",
        "\n",
        "# 2. print positive lexicon & negative lexicon:\n",
        "\n",
        "print(\"Positive Lexicon:\", sorted(positive_words))\n",
        "print(\"Negative Lexicon:\", sorted(negative_words))\n",
        "\n",
        "\n",
        "# --- Interactive Sentiment Testing ---\n",
        "print(\"\\nEnter sentences to analyze sentiment (type 'exit' to quit):\")\n",
        "while True:\n",
        "    text = input('> ').strip()\n",
        "    if text.lower() in ('exit', 'quit'):\n",
        "        print(\"Goodbye!\")\n",
        "        break\n",
        "\n",
        "    tokens = clean_text(text)\n",
        "    pos_count = sum(1 for t in tokens if t in positive_words)\n",
        "    neg_count = sum(1 for t in tokens if t in negative_words)\n",
        "    total = len(tokens)\n",
        "\n",
        "# 3. Compute simple sentiment score (hint: positive - negative count)\n",
        "\n",
        "    score = (pos_count - neg_count)\n",
        "\n",
        "    # Determine sentiment label\n",
        "    if score > 0:\n",
        "        sentiment = 'Positive'\n",
        "    elif score < 0:\n",
        "        sentiment = 'Negative'\n",
        "    else:\n",
        "        sentiment = 'Neutral'\n",
        "\n",
        "# 4. print the output results\n",
        "    print(f\"Tokens: {tokens}\")\n",
        "    print(f\"+ matches: {pos_count}, - matches: {neg_count}\")\n",
        "    print(f\"Score: {score:.3f} => {sentiment}\\n\")\n",
        "\n",
        "# 5. Add a short reflection as comments at the bottom (2–3 sentences)\n",
        "\n",
        "\"\"\"\n",
        "Strengths: This approach is simple to implement and fast to execute, making it suitable for basic sentiment analysis tasks.\n",
        "The lexicon-based method provides transparent results that are easy to interpret.\n",
        "\n",
        "Limitations: It lacks context understanding (e.g., sarcasm or negations like \"not happy\")\n",
        "and cannot handle domain-specific language without custom lexicons. The binary word matching\n",
        "oversimplifies the complexity of human sentiment.\n",
        "\"\"\"\n"
      ]
    }
  ]
}