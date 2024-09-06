import tkinter as tk
from tkinter import messagebox
import sqlite3

class EscolaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Passeio Escolar")

        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        # Criação dos widgets
        self.label = tk.Label(self.root, text="Nome do Aluno:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)

        self.button_add = tk.Button(self.root, text="Adicionar Aluno", command=self.add_aluno)
        self.button_add.grid(row=0, column=2, padx=10, pady=10)

        self.listbox = tk.Listbox(self.root, width=50, height=15)
        self.listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.button_confirm = tk.Button(self.root, text="Confirmar", command=self.confirmar)
        self.button_confirm.grid(row=2, column=0, padx=10, pady=10)

        self.button_paid = tk.Button(self.root, text="Marcar como Pago", command=self.marcar_pago)
        self.button_paid.grid(row=2, column=1, padx=10, pady=10)

        self.button_update = tk.Button(self.root, text="Atualizar", command=self.load_data)
        self.button_update.grid(row=2, column=2, padx=10, pady=10)

    def add_aluno(self):
        nome = self.entry_nome.get()
        if nome:
            conn = sqlite3.connect('escola.db')
            c = conn.cursor()
            c.execute('INSERT INTO alunos (nome, confirmado, pago) VALUES (?, ?, ?)', (nome, False, False))
            conn.commit()
            conn.close()
            self.entry_nome.delete(0, tk.END)
            self.load_data()
        else:
            messagebox.showwarning("Aviso", "O nome do aluno não pode estar vazio.")

    def load_data(self):
        self.listbox.delete(0, tk.END)
        conn = sqlite3.connect('escola.db')
        c = conn.cursor()
        c.execute('SELECT id, nome, confirmado, pago FROM alunos')
        for row in c.fetchall():
            status = "Confirmado" if row[2] else "Não Confirmado"
            pago = "Pago" if row[3] else "Não Pago"
            self.listbox.insert(tk.END, f"{row[1]} - {status} - {pago} - ID: {row[0]}")
        conn.close()

    def confirmar(self):
        selected_item = self.listbox.curselection()
        if selected_item:
            aluno_id = self.get_id_from_selection(selected_item[0])
            conn = sqlite3.connect('escola.db')
            c = conn.cursor()
            c.execute('UPDATE alunos SET confirmado = ? WHERE id = ?', (True, aluno_id))
            conn.commit()
            conn.close()
            self.load_data()
        else:
            messagebox.showwarning("Aviso", "Nenhum aluno selecionado.")

    def marcar_pago(self):
        selected_item = self.listbox.curselection()
        if selected_item:
            aluno_id = self.get_id_from_selection(selected_item[0])
            conn = sqlite3.connect('escola.db')
            c = conn.cursor()
            c.execute('UPDATE alunos SET pago = ? WHERE id = ?', (True, aluno_id))
            conn.commit()
            conn.close()
            self.load_data()
        else:
            messagebox.showwarning("Aviso", "Nenhum aluno selecionado.")

    def get_id_from_selection(self, index):
        selected_text = self.listbox.get(index)
        return int(selected_text.split("ID: ")[1])

if __name__ == "__main__":
    root = tk.Tk()
    app = EscolaApp(root)
    root.mainloop()
