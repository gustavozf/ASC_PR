% ======================================================
% SCRIPT PARA COMPUTAR LBP DAS IMAGENS DE CARTAS
% ALGORITMO DE http://www.cse.oulu.fi/MVG/Downloads/LBPMatlab
% UNIVERSIDADE OULU - MAENPPA.
% VERSÃO 0.3.2
% ======================================================

function chamaRLBP_zonas_mel_Acoustic_scene_com_rotulo_1025NEW(folder, segmentos, zonas, str_fold, classi, desc)
    clc;
    %folder = uigetdir; 
    %dirListing = dir(folder);
    lin  = 0;
    %segmentos=1;
    %zonas=15;
    %str_fold='acoustic_scene_Mel';
    cont =1;

    for zon=0:(zonas-1)
        for seg=0:(segmentos-1)
            %nome = strcat(str_fold,'-',num2str(zon),'-',num2str(seg),'-sem_rot.txt') ;
            nome_rot = strcat(str_fold,'-', classi, '-',num2str(zon),'-',num2str(seg),'.txt') ;
            fid = fopen(nome_rot,'w');  % NOME DO ARQUIVO DE SAÍDA COM RÓTULO
            %fid_sem_rot = fopen(nome,'w');  % NOME DO ARQUIVO DE SAÍDA SEM RÓTULO

            %for d = 3:length(dirListing)

            %if (dirListing(d).isdir == 1)

                fileName = fullfile(folder); % Abre a pasta....

                fopen(fileName);

               arquivos = dir(folder); % carrega as imagens....

                    for i = 3 : length(arquivos) %começa em 3 pois os dois primeiros são: . e ..
                        disp(cont);
                        cont = cont +1;
                        if (arquivos(i).isdir == 0)

                                 nomeArquivo = fullfile(fileName,arquivos(i).name); 
                                %  Possible values for MAPPINGTYPE are
                                %       'u2'   for uniform LBP
                                %       'ri'   for rotation-invariant LBP
                                %       'riu2' for uniform rotation-invariant LBP.
                                fopen(fileName);%nomeArquivo)
                                lin = lin + 1;   

                                I = imread(nomeArquivo); % Lê imagem.
                                [altura, largura]=size(I);

                                mapping=getmapping(8,'u2');

                                %linha1=round((zon/zonas*altura));
                                %if linha1==0
                                %     linha1=1;
                                %end;
                                %linha2=round((zon+1)/zonas*altura);

                                coluna1=round(((seg/segmentos)*largura));
                                if coluna1==0
                                      coluna1=1;                            
                                end;
                                coluna2=round(((seg+1)/segmentos)*largura);

                                switch (zon)
                                    case 0
                                       linha1= 1;
                                       linha2= 333;
                                    case 1
                                       linha1= 333;
                                       linha2= 362;
                                    case 2
                                       linha1= 362;
                                       linha2= 384;
                                    case 3
                                       linha1= 384;
                                       linha2= 417;
                                    case 4
                                       linha1= 417;
                                       linha2= 434;
                                    case 5
                                       linha1= 434;
                                       linha2= 443;
                                    case 6
                                       linha1= 443;
                                       linha2= 466;                      
                                    case 7
                                       linha1= 466;
                                       linha2= 490;
                                    case 8
                                       linha1= 489;
                                       linha2= 493;
                                    case 9
                                       linha1= 492;
                                       linha2= 497; 
                                    case 10
                                       linha1= 497;
                                       linha2= 504;
                                    case 11
                                       linha1= 504;
                                       linha2= 509;
                                    case 12
                                       linha1= 506;
                                       linha2= 510;
                                    case 13
                                       linha1= 509;
                                       linha2= 513;
                                    case 14
                                       linha1= 509;
                                       linha2= 513;
                                end

                                switch(desc)
                                    case 1
                                        H1=RLBP(I(linha1:linha2,coluna1:coluna2),2,8,mapping,'nh'); % nh = histograma normalizado.... 8 vizinhos
                                    case 2
                                        H1 = lpq(I(linha1:linha2,coluna1:coluna2),3);
                                    case 3
                                        H1 = lbp(I(linha1:linha2,coluna1:coluna2),2,8,mapping,'nh');
                                end 

                                %Salvando em arquivo....

                                fprintf(fid, '%f ', H1 ); %k, VetorDissimilaridade(lin,k));
                                fprintf(fid, '%s ', arquivos(i).name);

                                %fprintf(fid_sem_rot, '%f ', H1 );


                                fprintf(fid,'\n');
                                %fprintf(fid_sem_rot,'\n');

                                arquivoSaida(lin,:) = H1;
                                clear I mapping H1;
                        end

                    end

            %end 
            %end

        %save (nome, arquivoSaida, '-ascii'); % NOME DO ARQUIVO DE SAÍDA SEM OS RÓTULOS.

        fclose ( fid );
        %fclose ( fid_sem_rot );

        end
    end
end