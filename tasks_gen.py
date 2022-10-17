import re
import random
import pymorphy2
from docx import Document
from docx.shared import Pt


class TextProcessor:
    def __init__(self):
        self.original_text = []

    def tokenized_text(self):
        with open('text', 'r', encoding='utf-8') as f:
            texts = f.read()
            text = re.split(r'[#\n]', texts)
            for elem in text:
                if elem == '':
                    text.remove(elem)
                else:
                    self.original_text.append(re.split(r'[.?!]', elem))
        return self.original_text

class Generator:
    def __init__(self, text: TextProcessor):
        self.text = text.tokenized_text()
        self.original_texts = random.sample(self.text, 4)
        self.task_1()
        self.task_2()
        self.task_3()
        self.task_4()

    def task_1(self):
        text = self.original_texts[0]
        words = []
        for sent in text:
            word = sent.split()
            random.shuffle(word)
            words.append(word)
        return [self.original_texts, '. '.join(' '.join(x) for x in words)]

    def task_2(self):
        morph = pymorphy2.MorphAnalyzer()
        text = self.original_texts[1]
        words = []
        for sent in text:
            for word in sent.lower().split():
                p = morph.parse(word)[0]
                if p.tag.POS == 'VERB':
                    word = morph.parse(word)[0].normal_form
                words.append(word)
        return ' '.join(words)

    def task_3(self):
        text = self.original_texts[2]
        words = []
        for sentence in text:
            if sentence == '':
                text.remove(sentence)
            else:
                words.append(sentence.split())
        parts_1 = []
        parts_2 = []
        for sent in words:
            parts_1.append(' '.join(sent[:len(sent) // 2]))
            parts_2.append(' '.join(sent[len(sent) // 2:]))
        random.shuffle(parts_2)
        exercise_3 = []
        for i in zip(parts_1, parts_2):
            exercise_3.append(list(i))
        return exercise_3

    def task_4(self):
        text = self.original_texts[3]
        words = []
        for sentence in text:
            if sentence != '':
                words.append(sentence.split())
        answers = []
        final = []
        counter = 1
        for sentence in words:
            index = random.randint(0, len(sentence) - 1)
            answers.append(sentence[index])
            sentence[index] = '({})'.format(counter)
            counter += 1
            final.append(' '.join(sentence))
        random.shuffle(answers)
        exercise_4 = ['. '.join(final), answers]
        return exercise_4

class Saving:
    def __init__(self, saved_task):
        self.saved_task = saved_task
        self.save()

    def save(self):
        doc_orig = Document()
        style = doc_orig.styles['Normal']
        style.font.name = 'Times New Roman'
        style.font.size = Pt(14)
        doc_orig.add_paragraph('\n '.join('. '.join(x) for x in self.saved_task.task_1()[0]))
        doc_orig.save('/Users/a123/Desktop/tasks_2.docx')
        doc = Document()
        style = doc.styles['Normal']
        style.font.name = 'Times New Roman'
        style.font.size = Pt(14)
        doc.add_paragraph('Первое задание: поставьте слова в правильном порядке.')
        doc.add_paragraph(self.saved_task.task_1()[1])
        doc.add_paragraph('Второе задание: поставьте глаголы в нужную по контексту форму и расставьте знаки препинания.')
        doc.add_paragraph(self.saved_task.task_2())
        doc.add_paragraph('Третье задание: соедините части предложения.')
        table_3 = doc.add_table(rows=1, cols=2)
        table_3.style = 'Table Grid'
        row_3 = table_3.rows[0].cells
        row_3[0].text = 'Начало'
        row_3[1].text = 'Конец'
        for parts in self.saved_task.task_3():
            row_3 = table_3.add_row().cells
            row_3[0].text = parts[0]
            row_3[1].text = parts[1]
        doc.add_paragraph('Четвертое задание: вставьте слова.')
        table_4 = doc.add_table(rows=1, cols=2)
        table_4.style = 'Table Grid'
        row_4 = table_4.rows[0].cells
        row_4[0].text = 'Слово'
        row_4[1].text = 'Номер'
        for elem in self.saved_task.task_4():
            if type(elem) == str:
                doc.add_paragraph('\n' + elem)
            else:
                for word in elem:
                    row_4 = table_4.add_row().cells
                    row_4[0].text = word
                    row_4[1].text = ''
        doc.save('/Users/a123/Desktop/tasks_1.docx')

def task_gen(task_for_save):
    text_proc = TextProcessor()
    generate_tasks = Generator(text_proc)
    saving = Saving(generate_tasks)
    task_gen(saving)
