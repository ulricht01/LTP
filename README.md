# DOCKER-COMPOSE.YAML

## FLASK-MC
Flask využíváme k vytvoření webové aplikace, na které se zaregistrujeme a to nás zaeviduje do "White-Listu"
#### <i>````BUILD````</i>
Značí, že image pro tuto službu bude vytvořeno z aktuálního adresáře
#### <i>````CONTAINER_NAME````</i>    
Stanovuje název kontejneru pro Flask aplikaci
#### <i>````PORTS````</i> 
Představuje mapování portu pro Flask aplikaci
#### <i>````VOLUMES````</i> 
Připojuje dvě složky z hostitelského systému ke kontejneru - ./code a ./minecraft-data
#### <i>````DEPENDS_ON````</i> 
Říká, že tato služba závisí na službě mariadb-mc a nebude spuštěna, dokud není ta druhá připravena

## MARIADB-MC
Zachovává informace o zaregistrovaných hráčích
#### <i>````IMAGE````</i>  
Používá oficiální image MariaDB z Docker Hub
#### <i>````RESTART````</i> 
Nastavuje restartování kontejneru v případě selhání
#### <i>````ENVIRONMENT:MYSQL_ROOT_PASSWORD````</i> 
Nastavuje heslo pro uživatele root v MariaDB
#### <i>````VOLUMES````</i>  
Připojuje složku ./data z hostitelského systému ke složce s daty MariaDB uvnitř kontejneru
#### <i>````PORTS````</i> 
Mapuje port 3306 z hostitelského systému na port 3306 uvnitř kontejneru

## MINECRAFT-SERVER
Toto je náš MC server
#### <i>````IMAGE````</i> 
Používá image pro Minecraft server z Docker Hub
#### <i>````PORTS````</i> 
Představuje mapování portu pro MariaDB
#### <i>````ENVIRONMENT````</i> 
Nastavuje několik prostředí pro konfiguraci Minecraft serveru
#### <i>````VOLUMES````</i> 
Připojuje složku ./minecraft-data z hostitelského systému ke složce /data uvnitř kontejneru
#### <i>````RESTART````</i> 
Nastavuje restartování kontejneru v případě selhání

## PHPMYADMIN-MC
Pro jednudušší správu databáze a vizualizaci
#### <i>````IMAGE````</i> 
Používá image pro PhpMyAdmin z Docker Hub
#### <i>````CONTAINER_NAME````</i> 
Stanovuje název kontejneru pro PhpMyAdmin
#### <i>````DEPENDS_ON````</i> 
Říká, že tato služba závisí na službě mariadb-mc a nebude spuštěna, dokud není ta druhá připravena
#### <i>````ENVIRONMENT````</i> 
Nastavuje několik prostředí pro konfiguraci PhpMyAdmin, včetně toho, aby se připojil k MariaDB kontejneru
#### <i>````PORTS````</i> 
Představuje mapování portu pro PhpMyAdmin

# REQUIREMENTS
Soubor balíčků, které jsou potřeba pro chod aplikace

# DOCKERFILE
Tento Dockerfile vytváří kontejner pro Python aplikaci, která se připojuje k MariaDB databázi. Postupně nastavuje pracovní adresář, instaluje systémové závislosti pro MariaDB a Python, kopíruje soubory "requirements.txt" a "app.py" do kontejneru, a nakonec definuje příkaz pro spuštění aplikace, která komunikuje s MariaDB pomocí nastavených prostředních proměnných pro připojení

# CODE

#### <i>STATIC</i> 
Obsahuje kaskádové styly pro naší webovou stránku
#### <i>TEMPLATE</i> 
Obsahuje šablonu naší HTML stránky
#### <i>APP.py</i> 
Soubor obsahující metody, které nastavují webovou aplikaci a registraci pro "White-List"
#### <i>APP_LOGIC.py</i> 
Soubor obsahující metodu, která se stará o přeformátování a nahrání "White-Listu" do příslušného adresáře
#### <i>DATABASE.py</i> 
Soubor obsahující metody, které se starají o vytvoření, konektivitu a práci s databází
