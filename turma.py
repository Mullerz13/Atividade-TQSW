class Turma:
  def __init__(self):
    self.turma = [];
    self.menorNota = None;
    self.maiorNota = None;

  def cadastrarAlunos(self, alunos):
    # Valida todas as notas antes de cadastrar os alunos
    for aluno in alunos:
      if not 0 <= aluno.nota <= 10:
        raise ValueError(
          f"Nota inválida para {aluno.nome}: {aluno.nota}. "  
          "A nota deve estar entre 0 e 10."
        )

    for aluno in alunos:
      self.turma.append(aluno)

      if (self.menorNota is None or  aluno.nota < self.menorNota.nota):
            self.menorNota = aluno

      if (self.maiorNota is None or aluno.nota > self.maiorNota.nota):
        self.maiorNota = aluno

  def mostrarAlunos(self):
    print('Quantidade de alunos:', len(self.turma))
    for aluno in self.turma:
      print(aluno.mostrarAluno())
