import codecs
import nltk
from nltk.tokenize import word_tokenize


# 실습 환경에 미리 설치가 됨
#nltk.download('punkt')


def count_words(input_text):
    """
    input_text 내 단어들의 개수를 세는 함수
    :param input_text: 텍스트
    :return: dictionary, key: 단어, value: input_text 내 단어 개수
    """
    # <ToDo>: key: 단어, value: input_text 내 단어 개수인 output_dict을 만듭니다.
    tokens = input_text.split()

    # 빈 딕셔너리 생성
    output_dict = {}

    # 각 단어의 빈도수 계산
    for word in tokens:
        if word in output_dict:
            output_dict[word] += 1
        else:
            output_dict[word] = 1

    return output_dict


def main():
    # 데이터 파일인 'text8_1m_part_aa.txt'을 불러옵니다.
    with codecs.open("practice1/data/text8_1m_part_aa.txt", "r", "utf-8") as html_f:
        text8_text = "".join(html_f.readlines())
    
    # 데이터 내 단어들의 개수를 세어봅시다.
    word_dict = count_words(text8_text)
    
    # 단어 개수를 기준으로 정렬하여 상위 10개의 단어를 출력합니다.
    top_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)[:10]
    print(top_words)

    return word_dict


if __name__ == "__main__":
    main()
