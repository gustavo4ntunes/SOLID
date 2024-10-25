# Princípios S.O.L.I.D.

Os princípios S.O.L.I.D. são diretrizes que ajudam desenvolvedores a criar sistemas de software mais organizados, flexíveis e fáceis de manter. S.O.L.I.D. é um acrônimo para cinco princípios fundamentais da programação orientada a objetos:

1. **Single Responsibility Principle (SRP)** - Uma classe deve ter apenas uma responsabilidade. Isso facilita o entendimento e manutenção, pois mudanças afetam apenas uma parte do sistema.

2. **Open/Closed Principle (OCP)** - O código deve estar aberto para extensão, mas fechado para modificações. Podemos adicionar funcionalidades sem alterar o código existente, o que preserva sua estabilidade.

3. **Liskov Substitution Principle (LSP)** - Classes derivadas devem substituir suas classes base sem afetar o comportamento do programa, garantindo modularidade e uso seguro da herança.

4. **Interface Segregation Principle (ISP)** - Classes não devem ser forçadas a implementar interfaces que não utilizam. Interfaces menores tornam o código mais reutilizável e fácil de entender.

5. **Dependency Inversion Principle (DIP)** - Módulos de alto nível não devem depender de módulos de baixo nível, mas de abstrações. Isso aumenta a flexibilidade e permite substituir componentes sem alterar o código principal.

Esses princípios tornam o software modular e escalável, facilitando sua evolução com o mínimo de impacto em funcionalidades existentes.

### Melhorias de Design no Código para Alinhamento ao S.O.L.I.D.

**Separação de responsabilidades na classe Funcionario**  
No código inicial, a classe `Funcionario` lidava com múltiplas responsabilidades: armazenar dados do funcionário, calcular o salário e também imprimir os detalhes. Isso violava o Princípio da Responsabilidade Única, pois uma classe deve ter apenas uma razão para mudar. Ao separar essas responsabilidades em diferentes classes (`Funcionario`, `CalculadoraSalario`, e `ImpressorDetalhes`), temos um código mais organizado e claro. Agora, cada classe possui uma função específica: `Funcionario` armazena os dados do funcionário, `CalculadoraSalario` cuida das regras de cálculo do salário, e `ImpressorDetalhes` exibe as informações. Dessa forma, o código permite que alterações em uma responsabilidade (como o cálculo do salário) não afetem outras funções, como a exibição dos detalhes. Isso torna o código mais estável e com menos chances de falhas em caso de modificações.

**Redução de Condicionais e Melhoria na Flexibilidade**  
A estrutura inicial usava várias condições (`if-elif`) para calcular o salário, baseado no tipo de contrato. Isso é um problema porque, ao adicionar um novo tipo de contrato, seria necessário modificar a classe `Funcionario`, o que não é viável a longo prazo. Essa abordagem quebra o Princípio Aberto/Fechado, pois o código deve estar aberto para extensões, mas fechado para modificações diretas.

No código atualizado, cada tipo de contrato (`Estagiário`, `CLT`, `PJ`) agora possui sua própria classe de cálculo de salário, como `CalculadoraSalarioEstagiario`, `CalculadoraSalarioCLT`, e `CalculadoraSalarioPJ`. Essa mudança permite que novos tipos de contratos sejam adicionados sem modificar a estrutura existente. Basta criar uma nova classe de cálculo para o contrato, mantendo a estabilidade do código principal.

**Redução da Dependência Direta entre Componentes**  
No código inicial, `Funcionario` dependia diretamente dos tipos específicos para calcular o salário, o que viola o Princípio da Inversão de Dependência. A classe `Funcionario` deveria depender de abstrações, não de implementações específicas. Na versão corrigida, `Funcionario` agora recebe uma calculadora de salário como parâmetro, permitindo que `Funcionario` funcione independentemente do tipo específico de contrato, utilizando apenas a calculadora fornecida. Esse ajuste torna o código modular e permite modificar ou estender os cálculos de salário sem alterar o comportamento principal da classe `Funcionario`, respeitando o Princípio da Inversão de Dependência e facilitando futuras expansões.

**Inclusão do Tipo de Contrato nas Calculadoras**  
Anteriormente, o tipo de contrato era armazenado como um atributo na classe `Funcionario`, mas ele estava presente apenas para definir o cálculo do salário. Com a introdução das classes de cálculo específicas, o tipo de contrato foi incluído diretamente em cada calculadora (`tipo`), eliminando a necessidade de verificá-lo manualmente. Agora, `Funcionario` pode obter o tipo de contrato diretamente da calculadora que está sendo usada, eliminando a possibilidade de erros causados pelo uso incorreto do tipo de contrato. Isso torna o código mais conciso e respeita o Princípio de Segregação de Interfaces, já que `Funcionario` não precisa saber detalhes internos do cálculo de salário.

**Delegação da Exibição para ImpressorDetalhes**  
Para simplificar o código e manter a classe `Funcionario` focada apenas em seus dados, a responsabilidade de imprimir os detalhes foi delegada à classe `ImpressorDetalhes`. Esse ajuste permite que `Funcionario` se preocupe apenas com suas informações, enquanto `ImpressorDetalhes` gerencia a exibição. Esse modelo respeita o Princípio da Substituição de Liskov, pois `Funcionario` pode ter sua estrutura expandida ou alterada sem impactar o processo de exibição.
#
