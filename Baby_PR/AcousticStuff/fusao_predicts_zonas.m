
%function [] = fusao_predicts(predict1, predict2)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
qtde_folds = 5;
% quantas zonas há para fusão
zonas = 5;
% Tipos que serão usados para fusão. Informar o tipo e o diretório
tipo = 'lbp';
dir_origem = '/home/gustavozf/Documentos/UEM/Projetos/Baby/base_americana/05_Predicts/x1500/audios/5_folds/32000Hz_90dB/';
dir_resultados = '/home/gustavozf/Documentos/UEM/Projetos/Baby/base_americana/06_Fusion/x1500/audios/5_folds/32000Hz_90dB/';
% Linear = 'zl'. Mel = 'mel'
escala = 'zl';
channel = 'Left_Channel/';
dir_config = strcat( tipo, '_', escala, '_', num2str(zonas), 'z_1s/', channel );
disp(dir_config);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Diretório para armazenar os resultados

dir_origem = strcat(dir_origem, dir_config);
dir_resultados = strcat(dir_resultados, dir_config);
% Cria o diretório
mkdir(dir_resultados);

% Para cada um dos I folds faz a fusão
for i = 1 : qtde_folds

    % Formata o i para 2 casas, 01, 02...
    numero = num2str(i);

    % Apenas pra informar o que está sendo feito
    disp( strcat('Iniciando fusão do fold ', num2str(i), '...') );
    pos = 0;
    % Para cada uma das zonas
    for z = 0 : zonas-1

        % Forma os nomes dos arquivos
        predict = strcat(dir_origem, 'fold', num2str(numero), '/', 'fold', num2str(numero), '-', escala, '-', num2str(z), '-0-', tipo, '.svm.predict' );

        % Carrega os arquivos na forma de uma matriz
        %p = load(predict);
        
        p = dlmread(predict, ' ', 1, 0); %load, comecando da segunda linha
        
        % São do mesmo tamanho porque são do mesmo fold, por isso só verifica 1
        [totLinha, totCol] = size(p) ;
        %[p2_totLinha, p2_totCol] = size(p2) ;

        %totLinha = totLinha + 1;
        %disp(totLinha);
        %disp(totCol);
        % Recebe a matriz sem aquela primeira linha com as classes
        %p_matrizVal = p(2: totLinha, : );
         p_matrizVal = p( : , : );

        
        % Adiciona os valores carregados numa matriz nova (que será a junção de
        % todos)
        %matrizJuncao(:,:,z) = p_matrizVal ;
        pos = pos + 1;
        if z == 0
            matrizJuncao = zeros(totLinha, totCol, zonas);
        end
        matrizJuncao(:,:,pos) = p_matrizVal ;
        
    end % fim das zonas

    % Prepara a matriz final. A primeira linha foi removida.
    % A primeira coluna não pode ser mais considerada porque ainda é a classe
    % que o SVM colocou no predict. É necessário fazer um novo julgamento.
    for lin = 1 : totLinha
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
    somaSaida = strcat(dir_resultados, 'fold-', num2str(numero),'-', escala, '-fusao-soma-', tipo, '.svm.predict' );
    produtoSaida = strcat(dir_resultados, 'fold-', num2str(numero),'-', escala, '-fusao-produto-', tipo, '.svm.predict' );
    maximoSaida = strcat(dir_resultados, 'fold-', num2str(numero),'-', escala, '-fusao-maximo-', tipo, '.svm.predict' );

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
    for l = 1 : totLinha
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
    clear nomeSaida p_matrizVal totLinha totCol p predict numero
    clear fileSoma fileProduto fileMaximo

    % Salva as Regras. Mas não será usado porque já será gerado o predict final.
    % save regraMaximoDS3_1.txt regraMaximo -ascii
    % save regraMinimoDS3_1.txt regraMinimo -ascii
    % save regraMediaDS3_1.txt regraMedia -ascii
    % save regraMedianaDS3_1.txt regraMediana -ascii
    % save regraProdutoDS3_1.txt regraProduto -ascii
    % save regraSomaDS3_1.txt regraSoma -ascii

end
