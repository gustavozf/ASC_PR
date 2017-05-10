%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Autor: Gustavo Zanoni Felipe
%Data: 23/04/2017
%Este algoritmo aplica os descritores: RLBP, LBP e LPQ.
%Podendo zonear e segmentar.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
entrada = '/home/gustavozf/Documentos/Projeto/Saidas/Espectrogramas/513new/'; %Diretorio dos Espectrogramas
saida = '/home/gustavozf/Documentos/Projeto/Saidas/OUT/'; %Saida com os features
desc = 3; %1 = RLBP, 2 = LPQ, 3 = LBP
tipo_zona = 1; %1 = Zonas Lineares / 2 = Escala Mel
segmentos = 1; %Numero de segmentos
zonas = 4; %Numero de zonas. PS.: Escala Mel = 15 Zonas!

switch (desc)
    case 1
        descritor = 'rlbp';
    case 2
        descritor = 'lpq';
    case 3
        descritor = 'lbp';
end
switch (tipo_zona)
    case 1 
        str_fold =  'zl';
    case 2
        str_fold =  'mel';
end

%examplo de saida: saida/lbp_mel_15z_1s
destino = strcat(saida,descritor, '_', str_fold, '_', num2str(zonas), 'z_', num2str(segmentos), 's/');
%can = {'Mono', 'Spectrograms1', 'Spectrograms2'};
%Caso haja canais (Canal esquerdo, direito ou esquerdo+direito (mono))
can = {'Spectrograms2'};
%Variar teste e treino
tes = {'test', 'train'};
%vetor com as classificacoes
classi = {'beach', 'bus', 'cafe-restaurant', 'car', 'city_center', 'forest_path', 'grocery_store', 'home', 'library', 'metro_station', 'office', 'park', 'residential_area', 'train', 'tram'};

for i = 1 : length(can) %varia entre os canais
    for j = 1 : length(tes) %varia teste e treino
        for z = 1 : 4 %varia pelo numero de folds
            for k = 1:length(classi) %varia as classificacoes
            fold = strcat(entrada, can{i}, '/', tes{j}, '/fold', num2str(z), '/', classi{k}, '/');
            saida = strcat(destino, can{i},'/', tes{j}, '/fold', num2str(z), '/', classi{k}, '/');
            mkdir(saida); %faz o diretorio da saida
            switch (tipo_zona)
                case 1 
                    chamaRLBP_zonas_linearNEW(fold, segmentos, zonas, str_fold, classi{k}, desc);
                case 2
                    chamaRLBP_zonas_mel_Acoustic_scene_com_rotulo_1025NEW(fold, segmentos, zonas, str_fold, classi{k}, desc);
            end
            movefile('*.txt', saida);
            end
        end
    end
end