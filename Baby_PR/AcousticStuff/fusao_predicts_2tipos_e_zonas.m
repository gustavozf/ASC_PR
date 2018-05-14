
%function [] = fusao_predicts(predict1, predict2)

qtde_folds = 10;

% Tipos que serão usados para fusão. Informar o tipo e o diretório
tipo1 = 'lbp';
% Se tiver alguma escala certa, coloque '-nome'
escala1 = '-mel';
dir_origem_tipo1 = '/media/rafael/Dados/Mestrado/base_teste_nr_filtrada_z65_mel2/';
% Tipo e diretório
tipo2 = 'rp';
dir_origem_tipo2 = '/media/rafael/Dados/Mestrado/Base_filtrada_teste_justo_concatenada_af_rp/';

% Diretório para armazenar os resultados
dir_resultados = strcat('teste_',tipo1, '_mel2_', tipo2);
dir_path = '/media/rafael/Dados/Mestrado/';
% Cria o diretório
mkdir(dir_path,dir_resultados);
dir_resultados = strcat(dir_path, dir_resultados, '/');

% Para cada um dos I folds faz a fusão
for i = 1 : qtde_folds
    
    % Formata o i para 2 casas, 01, 02...
    numero = num2str(i, '%02i');
    
    % Forma os nomes dos arquivos 
    predict1 = strcat(dir_origem_tipo1, 'fold-', num2str(numero), escala1, '-fusao-soma-', tipo1, '.svm.predict' );
    predict2 = strcat(dir_origem_tipo2, 'fold-', num2str(numero), '-', tipo2, '.svm.predict' );
    
    % Carrega os arquivos na forma de uma matriz
    p1 = load(predict1);
    p2 = load(predict2);

    % São do mesmo tamanho porque são do mesmo fold, por isso só verifica 1
    [totLinha, totCol] = size(p1) ;
    %[p2_totLinha, p2_totCol] = size(p2) ;

    %totLinha = totLinha + 1;

    % Recebe a matriz sem aquela primeira linha com as classes
    p1_matrizVal = p1(2: totLinha, : );
    p2_matrizVal = p2(2: totLinha, : );

    % Adiciona os valores carregados numa matriz nova (que será a junção de
    % todos)
    matrizJuncao(:,:,1) = p1_matrizVal ;
    matrizJuncao(:,:,2) = p2_matrizVal ;

    % Prepara a matriz final. A primeira linha foi removida.
    % A primeira coluna não pode ser mais considerada porque ainda é a classe
    % que o SVM colocou no predict. É necessário fazer um novo julgamento.
    for lin = 1 : (totLinha - 1)
        for col = 1 : totCol

                regraSoma(lin,col)    = sum(matrizJuncao(lin,col,:));
                regraProduto(lin,col) = prod(matrizJuncao(lin,col,:));
                regraMaximo(lin,col)  = max(matrizJuncao(lin,col,:));
                
                regraMediana(lin,col) = median(matrizJuncao(lin,col,:));
                regraMinimo(lin,col)  = min(matrizJuncao(lin,col,:));
                regraMedia(lin,col)   = mean(matrizJuncao(lin,col,:));

        end
    end

    %%% Gerando o predict final já com o julgamento %%%

    % Definindo o nome do arquivo
    somaSaida = strcat(dir_resultados, 'fold-', num2str(numero), '-fusao-soma-', tipo1, '-', tipo2, '.svm.predict' );
    produtoSaida = strcat(dir_resultados, 'fold-', num2str(numero), '-fusao-produto-', tipo1, '-', tipo2, '.svm.predict' );
    maximoSaida = strcat(dir_resultados, 'fold-', num2str(numero), '-fusao-maximo-', tipo1, '-', tipo2, '.svm.predict' );

    % Cria o arquivo vazio
    fileSoma = fopen(somaSaida,'w');
    fileProduto = fopen(produtoSaida,'w');
    fileMaximo = fopen(maximoSaida,'w');

    % Apenas para preencher um número e não a palavra classe ou rótulo
    fprintf(fileSoma, '%d ', 9999);
    fprintf(fileProduto, '%d ', 9999);
    fprintf(fileMaximo, '%d ', 9999);

    % Preenche a partir da segunda coluna
    for c = 0 : (totCol - 2)
        fprintf(fileSoma, '%d ', c);
        fprintf(fileProduto, '%d ', c);
        fprintf(fileMaximo, '%d ', c);
    end

    % Pula uma linha
    fprintf(fileSoma, ' \n');
    fprintf(fileProduto, ' \n');
    fprintf(fileMaximo, ' \n');
    
    % Percorre todas as linhas e colunas
    for l = 1 : totLinha - 1
        for c = 1 : totCol

            % A primeira coluna tem que ter o a classe do predict
            if c == 1
                % Busca o maior valor e o índice dele.
                % Só usamos o índice porque é a classe.
                % Os vetores de regra não tem a primeira linha (rótulo)
                [maxValueSoma, indexSoma] = max(regraSoma( l ,2:totCol));
                [maxValueProduto, indexProduto] = max(regraProduto( l ,2:totCol));
                [maxValueMaximo, indexMaximo] = max(regraMaximo( l ,2:totCol));
                % A classe começa em 0, por isso -1
                fprintf(fileSoma, '%d ', indexSoma-1);
                fprintf(fileProduto, '%d ', indexProduto-1);
                fprintf(fileMaximo, '%d ', indexMaximo-1);

            else
                % Busca o resultado do predict após a operação
                xS = regraSoma( l , c );
                xP = regraProduto( l , c );
                xM = regraMaximo( l , c );
                % limita as casas decimais porque já foi julgado
                fprintf(fileSoma, '%.6f ', xS);
                fprintf(fileProduto, '%.6f ', xP);
                fprintf(fileMaximo, '%.6f ', xM);

            end

        end

        % Vai para a próxima linha
        fprintf(fileSoma, ' \n');
        fprintf(fileProduto, ' \n');
        fprintf(fileMaximo, ' \n');
    end

    fclose(fileSoma);
    fclose(fileProduto);
    fclose(fileMaximo);
    
    % Limpando as variáveis
    clear regraSoma regraProduto regraMediana regraMaximo regraMinimo regraMedia matrizJuncao
    clear nomeSaida p1_matrizVal p2_matrizVal totLinha totCol p1 p2 predict1 predict2 numero
    clear fileSoma fileProduto fileMaximo
    
    % Salva as Regras. Mas não será usado porque já será gerado o predict final.
    % save regraMaximoDS3_1.txt regraMaximo -ascii
    % save regraMinimoDS3_1.txt regraMinimo -ascii
    % save regraMediaDS3_1.txt regraMedia -ascii
    % save regraMedianaDS3_1.txt regraMediana -ascii
    % save regraProdutoDS3_1.txt regraProduto -ascii
    % save regraSomaDS3_1.txt regraSoma -ascii
    
end
