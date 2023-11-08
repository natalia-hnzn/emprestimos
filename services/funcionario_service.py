from PySide6.QtWidgets import QMessageBox

from infra.entities.funcionario import Funcionario
from infra.repository.emprestimo_repository import EmprestimoRepository
from infra.repository.funcionario_repository import FuncionarioRepository
from infra.repository.uniforme_repository import UniformeRepository
from services.main_window_service import MainWindowService


class FuncionarioService:
    def __init__(self):
        self.service_main_window = MainWindowService()
        self.emprestimo_repository = EmprestimoRepository()
        self.uniforme_repository = UniformeRepository()
        self.funcionario_repository = FuncionarioRepository()

    def insert_funcionario(self, main_window):
        funcionario = Funcionario()
        funcionario.nome = main_window.txt_nome_funcionario.text()
        funcionario.cpf = main_window.txt_cpf_funcionario.text()
        funcionario.ativo = True
        try:
            self.funcionario_repository.insert_one_funcionario(funcionario)
            main_window.txt_nome_funcionario.setText('')
            main_window.txt_cpf_funcionario.setText('')
            self.service_main_window.populate_table_funcionario(main_window)
            QMessageBox.information(main_window, 'Funcionários', f'Funcionário cadastrado com sucesso')
        except Exception as e:
            QMessageBox.warning(main_window, 'Funcionários', f'Erro ao cadastrar funcionário.\nErro : {e}')

    def select_funcionario(self, emprestimo_ui):
        if emprestimo_ui.btn_consulta_funcionario.text() == 'Limpar':
            emprestimo_ui.txt_nome_funcionario_emprestimo.setText('')
            emprestimo_ui.txt_cpf_funcionario_emprestimo.setText('')
            emprestimo_ui.txt_cpf_funcionario_emprestimo.setReadOnly(False)
            emprestimo_ui.selected_funcionario = None
            emprestimo_ui.btn_consulta_funcionario.setText('Consultar')
        else:
            try:
                if emprestimo_ui.txt_cpf_funcionario_emprestimo.text() != '':
                    funcionario_emprestimo = self.funcionario_repository. \
                        select_funcionario_by_cpf(emprestimo_ui.txt_cpf_funcionario_emprestimo.text())
                    emprestimo_ui.selected_funcionario = funcionario_emprestimo
                    emprestimo_ui.txt_nome_funcionario_emprestimo.setText(funcionario_emprestimo.nome)
                    emprestimo_ui.txt_cpf_funcionario_emprestimo.setReadOnly(True)
                    emprestimo_ui.btn_consulta_funcionario.setText('Limpar')
                else:
                    QMessageBox.warning(emprestimo_ui, 'Funcionários', f'Insira um CPF para consultar funcionário.')
            except Exception as e:
                QMessageBox.warning(emprestimo_ui, 'Funcionários', f'Erro ao consultar funcionário.\nErro : {e}')

                emprestimo_ui.txt_nome_funcionario_emprestimo.clear()

    def update_funcionario(self, main_window):
        if main_window.btn_editar_funcionario.text() == 'Editar':
            selected_rows = main_window.tb_funcionario.selectedModel().selectedRows()
            if not selected_rows:
                QMessageBox.warning(main_window, 'Funcionários', f'Selecione um funcionário')
                return
            selected_row = selected_rows[0]
            main_window.txt_nome_funcionario.setText(main_window.tb_funcionario.item(selected_row, 0).text())
            main_window.txt_cpf_funcionario.setText(main_window.tb_funcionario.item(selected_row, 1).text())
