from wordcloud import WordCloud
import matplotlib.pyplot as plt
import compare
from matplotlib.lines import Line2D

class Compare2ColorFunc():
  def __init__(self, shared_text, stopwords):
    self.shared_text = shared_text
    self.stopwords = stopwords

  def __call__(self,word,font_size,position,orientation,random_state=None,**kwargs):
    if word in self.shared_text:
        if appearances(word, self.shared_text) == max_appearing_val(self.shared_text, self.stopwords):
            return f'rgb(255, 0, 0)'
        elif appearances(word, self.shared_text) >= max_appearing_val(self.shared_text, self.stopwords)/2:
            return f'rgb(175, 0, 0)'
        else:
            return f'rgb(100, 0, 0)'
    else:
        return 'rgb(0, 0, 0)'
    
class Compare3ColorFunc():
    def __init__(self, shared_text1, shared_text2, stopwords):
        self.shared_text1 = shared_text1
        self.shared_text2 = shared_text2
        self.stopwords = stopwords
    
    def __call__(self,word,font_size,position,orientation,random_state=None,**kwargs):
        if word in self.shared_text1 and word in self.shared_text2:
            return f'rgb(0, 0, 255)'
        elif word in self.shared_text1:
            return f'rgb(255, 0, 0)'
        elif word in self.shared_text2:
            return f'rgb(0, 255, 0)'
        else:
            return 'rgb(0, 0, 0)'

                
    
def max_appearing_val(shared_text, STOPWORDS=None):
    max_val = 0
    for word in shared_text.split():
        if shared_text.count(word) > max_val and word not in STOPWORDS:
            print(word, shared_text.count(word))
            max_val = shared_text.count(word)
    return max_val

def appearances(word, shared_text):
    return shared_text.count(word)

#compares two files, intensity of color is how many times it appears in the shared words list
def compare_two_files(main_file, comparison_file):
    shared_text = compare.shared_words(main_file, comparison_file)
    shared_text = ' '.join(shared_text)
    text = compare.read_file(main_file)
    text = ' '.join(text)
    wordcloud = WordCloud(background_color='white')
    STOPWORDS = wordcloud.stopwords
    wordcloud.generate(text)
    wordcloud.recolor(color_func=Compare2ColorFunc(shared_text, STOPWORDS))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f'Words in {main_file}\nComparison to {comparison_file}\n')
    plt.axis("off")
    plt.legend()
    plt.show()

#compares three files, no longer cares about intensity, just where words show up
def compare_three_files(main_file, comparison_file1, comparison_file2):
    shared_text1 = compare.shared_words(main_file, comparison_file1)
    shared_text1 = ' '.join(shared_text1)
    shared_text2 = compare.shared_words(main_file, comparison_file2)
    shared_text2 = ' '.join(shared_text2)
    text = compare.read_file(main_file)
    text = ' '.join(text)
    wordcloud = WordCloud(background_color='white', prefer_horizontal=1, width=2000, height=500)
    STOPWORDS = wordcloud.stopwords
    wordcloud.generate(text)
    wordcloud.recolor(color_func=Compare3ColorFunc(shared_text1, shared_text2, STOPWORDS))
    fig, axs = plt.subplots(2)
    axs[1].imshow(wordcloud, interpolation='bilinear')
    axs[1].axis("off")
    
    custom_lines = [Line2D([0], [0], color=(255/255, 0/255, 0/255), lw=4),
                Line2D([0], [0], color=(0/255, 255/255, 0/255), lw=4),
                Line2D([0], [0], color=(0/255, 0/255, 255/255), lw=4),
                Line2D([0], [0], color=(0/255, 0/255, 0/255), lw=4)]
    axs[0].legend(custom_lines, [f'Words in {main_file} and {comparison_file1}', 
                              f'Words in {main_file} and {comparison_file2}', 
                              f'Words in all three files', 
                              f'Words only in {main_file}'])
    axs[0].axis("off")
    plt.show()

def main():
    compare_two_files('architecture_neutral.txt', 'architecture_man.txt')
    compare_three_files('architecture_neutral.txt', 'architecture_man.txt', 'architecture_woman.txt')

if __name__ == '__main__':
    main()