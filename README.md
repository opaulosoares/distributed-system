# MedTrack

Instruções e considerações sobre nosso projeto para a disciplina de Sistemas Distribuídos SSC-0904.

## (<span style="color:red">Importante</span>) Considerações sobre os recursos computacionais

Antes de começar a explicar sobre o _setup_ do projeto, achamos extremamente relevante pontuar o seguinte:

O nosso projeto foi feito com tecnologias como _kubernetes_ e _kind_ (_kubernetes in docker_) para sua elaboração. Porém, isso possui um custo computacional embutido.

Implementamos um projeto que foi testado diversas vezes em um computador com mais recurso do que a máquina virtual dada pela disciplina e não tivemos nenhum tipo de problema com serviços caindo. **Por isso não implementamos rotinas de verificação para reiniciá-los no caso de falta de recurso computacional.**

Assim, como o **recurso é compartilhado** entre os grupos, **é possível de um serviço nosso cair** e não ser reinicializado. Assim, o funcionamento da aplicação como um todo é comprometido. **<span style="color:red">Portanto, é possível que a versão que está no cluster não esteja funcionando.</span>**

Mas, caso a instalação seja feita novamente, de maneira que siga exatamente o que está nesse documento, o aplicativo roda assim como rodou na apresentação do dia 24/06/2024, como mostrado ao professor.

Vale ressaltar que mesmo com a expansão da memória da máquina virtual para 4GB (dada pelo professor após a apresentação), serviços como o Kafka falharam por falta de CPU, como pode ser visto na imagem a seguir, capturada no ArgoCD, que integramos no nosso projeto.

![Foto do serviço kafka](https://i.ibb.co/z7556gK/photo-2024-06-25-20-32-59.jpg)
Lê-se, em inglês, o erro: "_0/1 nodes are available. 1 Insufficient cpu..._"

## 1. Como iniciar o projeto

Antes de começar as instruções para iniciar o projeto, é relevante contextualizar que estamos assumindo que os recursos _docker_, _nodejs_, _python3_ com _pip_, _GNU Makefile_ estejam instalados no sistema. Também é relevante ressaltar que fizemos o projeto assumindo também que será rodado apenas no Linux (a conexão `ssh` pode ser feita de qualquer dispositivo). Vale a pena ressaltar que **todos comandos do Makefile** sejam rodados com o `sudo` e sejam acessados do terminal nativo do sistema operacional (os comandos de `ssh -L` com as portas não funcionam no WSL).

### Instalar _kubectl_, _kind_, _helm_

Agora vamos mostrar os comandos para instalar os recursos específicos do nosso projeto

1. Instale o _kubectl_

```sh
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

2. Instale o _kind_ (_kubernetes in docker_)

```sh
# For AMD64 / x86_64
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.23.0/kind-linux-amd64
# For ARM64
[ $(uname -m) = aarch64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.23.0/kind-linux-arm64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```

3. Instalar o _helm_

```sh
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
```

### Comandos Makefile para fazer deploy do projeto

1. Instalar as dependencias do Nodejs para frontend e backend

```sh
sudo make init
```

2. Fazer _build_ das imagens _docker_

```sh
sudo make build-images
```

3. Subir a aplicação completa

```sh
sudo make up
```

#### Caso qualquer problema aconteça/queira finalizar a aplicação

```sh
sudo make down
```

Na aplicação, nós utilizamos o gerenciador de pacotes para _Kubernetes_ chamado _helm_. Ele depende de acesso a internet e da disponibilidade dos servidores que oferecem os pacotes. Caso qualquer problema aconteça por problemas de rede, o comando acima deve ser executado, seguido pelo comando `sudo make up` para reiniciar o processo de _deploy_.