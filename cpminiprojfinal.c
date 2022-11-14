#include<stdio.h>
#include<string.h>
#include<conio.h>
#include<stdlib.h>
void guwahati();   //done
void shimla();     //done
void london();     //done
void kerala();     //done
void thailand();   //done
void rajasthan();  //done
void japan();      //done
void egypt();      //done
void ooty();       //done
void heading(){
   printf("***********************************************************************************************************************\n");
   printf("\t\t\t\t\t Welcome to New India Tours and Travels!\n");
   printf("\t\t\t\t\t ---------------------------------------\n");
   printf("\t  We offer some of the best and the most sought after tours of a variety of places in the world !\n");
   printf("\t  Hurry up and get upto 30%% on your next tour when you travel with us! (conditions apply)\n");
   printf("\t                   ---------                                            -----------------\n");
   printf("\t  For a tour in India or an International tour of more than 8 days, we are offering 15%% percent off! \n");
   printf("\t  Also, all values are in INR and base charge is per person.\n");
   printf("***********************************************************************************************************************\n");

}
void giveroominfindia(){
    FILE *fh;
    fh = fopen("C://Users/dkshi/Downloads/cpminiprojfiles/roomdomestic.txt","r");
  if(fh != NULL )
  {
    char c;
    while((c=fgetc(fh)) != EOF)
     putchar(c);
     fclose(fh);
  }
}
void giveroominfint(){
    FILE *fh;
    fh = fopen("C://Users/dkshi/Downloads/cpminiprojfiles/roomint.txt","r");
  if(fh != NULL )
  {
    char c;
    while((c=fgetc(fh)) != EOF)
     putchar(c);
     fclose(fh);
  }
}
typedef struct mynode
{
    char name[100];
    char gen[100];
    int age;
    struct mynode* link;
} Node;
Node* start = NULL;

void add_node();
void details();
int k, amount,ph,ph1,hotelcost[6],hotelcost1[2],sum,sum1,basecharge=0,room_cost[6]={1900,3000,3250,3850,4300,4800},room_cost1[2]={7200,10000},discountamt,n;
int guideind=500,guideint=2000,guidenum,guidenum1;
char type[100], place[100], date[100], addr[100],eml[100],mobile[10],mobile1[10];
struct room_info
{
    int choice_no[10];
    int room_frequency[10];
} r1;     //change size accordingly
void room(int m)
{
    int d=0;
    while(m>0)
    {
        printf("Enter room choice %d: ",d+1);
        scanf("%d",&r1.choice_no[d]);
        printf("Enter no. of rooms: ");
        scanf("%d",&r1.room_frequency[d]);
        if(r1.room_frequency[d]>m)
        {
            int e;
            printf("The number of rooms selected exceeds!\nDo you want to increase the number?\nSelect 1 for yes and 2 for no:");
            r:scanf("%d",&e);
            switch(e)
            {
                case 1:
                m=r1.room_frequency[d];
                break;
                case 2:
                r1.room_frequency[d]=m;
                break;
                default:
                {
                    printf("Enter the valid choice!!!");
                    goto r;
                }
            }
        }
        //use file handling here
        m=m-r1.room_frequency[d];
        d++;
    }
}
void hotelcharges(int j){
    r1.choice_no;
    room_cost[8];
    r1.room_frequency;
    int d=0;
    if(j<=5){
        for(int i=1;i<=6;i++){
            r1.choice_no[d];
            hotelcost[i]=(room_cost[d])*(r1.room_frequency[d]);
            d++;
        }
    }
    else{
        for(int i=1;i<=2;i++){
            r1.choice_no[d];
            hotelcost1[i]=(room_cost1[d])*(r1.room_frequency[d]);
            d++;
        }
    }
    if(j<=5){
        for(int i=0;i<6;i++){
            sum += hotelcost[i];
        }
        printf("%d",sum);
        if (j==1){
            sum=sum*5;
        }
        else if(j==2){
            sum=sum*5;
        }
        else if(j==3){
            sum=sum*7;
        }
        else if(j==4){
            sum=sum*11;
        }
        else if(j==5){
            sum=sum*6;
        }
        else
            printf("error!");
    }
    else{
        for(int i=0;i<2;i++){
            sum1 +=hotelcost1[i];
        }
        if (j==6){
            sum1=sum1*6;
        }
        else if(j==7){
            sum1=sum1*6;
        }
        else if(j==8){
            sum1=sum1*7;
        }
        else if(j==9){
            sum1=sum1*5;
        }
        else
            printf("error!");
        printf("%d",sum1);
    }

}
void discount(int j){
    if(j==1){
        discountamt=((basecharge*k)+sum+(guideind*guidenum))*1;
    }
    else if(j==2){
        discountamt=((basecharge*k)+sum+(guideind*guidenum))*1;
    }
    else if(j==3){
        discountamt=((basecharge*k)+sum+(guideind*guidenum))*0.85;
    }
    else if(j==4){
        discountamt=((basecharge*k)+sum+(guideind*guidenum))*0.85;
    }
    else if(j==5){
        discountamt=((basecharge*k)+sum+(guideind*guidenum))*1;
    }
    else if(j==6){
        discountamt=((basecharge*k)+sum1+(guideint*guidenum1))*1;
    }
    else if(j==7){
        discountamt=((basecharge*k)+sum1+(guideint*guidenum1))*1;
    }
    else if(j==8){
        discountamt=((basecharge*k)+sum1+(guideint*guidenum1))*0.85;
    }
    else if(j==9){
        discountamt=((basecharge*k)+sum1+(guideint*guidenum1))*1;
    }
    else
        printf("error!");
}
void receipt();
int main()
{
   int n1;
   heading();
   printf("Below is our index where the tours we currently offer are displayed.\n");
   printf("--------------------------------------------------------------------\n");
   printf("You may choose any tour of your liking and we will further proceed with the itinerary regarding it.\n");
   printf("---------------------------------------------------------------------------------------------------\n");
   printf("(Here D is for days and N is for nights)\n-----------------------------------------\n");
   printf("Also, the prices given with the tour are the price per person and exclusive of taxes.\n");
   printf("------------------------------------------------------------------------------------\n");
   printf("\nEnter any number from 1 to 9 for the tour of your choice: \n");
   printf("1.Guwahati tour(6D/5N)\n");
   printf("2.Shimla tour(6D/5N)\n");
   printf("3.Kerala tour(8D/7N)\n");
   printf("4.Ooty tour(12D/11N)\n");
   printf("5.Rajasthan tour(7D/6N)\n");
   printf("6.Thailand Tour(7D/6N)\n");
   printf("7.Japan tour(7D/6N)\n");
   printf("8.Egypt Tour(8D/7N)\n");
   printf("9.London & Paris tour(6D/5N)\n");
   scanf("\t %d",&n);
   switch(n)
   {
      case 1: {guwahati();

      n1=1;}
      break;
      case 2: {shimla();
      n1=1;}
      break;
      case 3: {kerala();
      n1=1;}
      break;
      case 4: {ooty();
      n1=1;}
      break;
      case 5: {rajasthan();
      n1=1;}
      break;
      case 6: {thailand();
      n1=2;}
      break;
      case 7: {japan();
      n1=2;}
      break;
      case 8: {egypt();
      n1=2;}
      break;
      case 9: {london();
      n1=2;}
      break;
      case 10:
      break;
      default:
      printf("invalid choice");
      break;

   }
    printf("\n\n\tYou have selected tour %d.\n",n);
    printf("\n\tWe will now take some traveler information. Press any button to continue.\n\t(Beware that the information given will disappear)\n");
    getch();
    details();
    system("cls");
    int n2;
    heading();
    if(n<=5){
        giveroominfindia();
    }
    else{
        giveroominfint();
    }
    printf("\nEnter the total number of rooms: \n");
    scanf("%d",&n2);
    room(n2);
    if(n<=5){
        printf("do you want guide ?\n");
        printf("If yes then enter for how many days or press 0 if you don't want a guide\n");
        scanf("%d",&guidenum);
    }
    else{
        printf("do you want guide ?\n");
        printf("If yes then enter for how many days or press 0 if you don't want a guide\n");
        scanf("%d",&guidenum1);
    }
    hotelcharges(n);
    discount(n);
    receipt();
    storedata();
    }
void guwahati()
{
 FILE *fh;
    fh = fopen("C://Users/dkshi/Downloads/cpminiprojfiles/guwahati.txt","r");
  if(fh != NULL )
  {
    char c;
    while((c=fgetc(fh)) != EOF)
     putchar(c);
     fclose(fh);
  }
  strcpy(place, "Guwahati Tour");
  basecharge=15000;

}
void shimla()
{
  FILE *fh;
    fh = fopen("C://Users/dkshi/Downloads/cpminiprojfiles/shimla.txt","r");
  if(fh != NULL )
  {
    char c;
    while((c=fgetc(fh)) != EOF)
     putchar(c);
     fclose(fh);
  }
  strcpy(place, "Shimla Tour");
  basecharge=12000;
}
void london()
{

  FILE *fh;
    fh = fopen("C://Users/dkshi/Downloads/cpminiprojfiles/london.txt","r");
  if(fh != NULL )
  {
    char c;
    while((c=fgetc(fh)) != EOF)
     putchar(c);
     fclose(fh);
  }
  strcpy(place, "London Tour");
  basecharge=25000;

}
void kerala()
{
    FILE *fh;
    fh = fopen("C://Users/dkshi/Downloads/cpminiprojfiles/kerala.txt","r");
  if(fh != NULL )
  {
    char c;
    while((c=fgetc(fh)) != EOF)
     putchar(c);
     fclose(fh);
  }
  strcpy(place, "Kerala Tour");
  basecharge=14000;
}
void thailand()
{
 FILE *fh;
    fh = fopen("C://Users/dkshi/Downloads/cpminiprojfiles/thailand.txt","r");
  if(fh != NULL )
  {
    char c;
    while((c=fgetc(fh)) != EOF)
     putchar(c);
     fclose(fh);
  }
  strcpy(place, "Thailand Tour");
  basecharge=27000;
}
void rajasthan()
{
  FILE *fh;
    fh = fopen("C://Users/dkshi/Downloads/cpminiprojfiles/rajasthan.txt","r");
  if(fh != NULL )
  {
    char c;
    while((c=fgetc(fh)) != EOF)
     putchar(c);
     fclose(fh);
  }
  strcpy(place, "Rajasthan Tour");
  basecharge=16000;
}
void japan()
{
  FILE *fh;
    fh = fopen("C://Users/dkshi/Downloads/cpminiprojfiles/japan.txt","r");
  if(fh != NULL )
  {
    char c;
    while((c=fgetc(fh)) != EOF)
     putchar(c);
     fclose(fh);
  }
  strcpy(place, "Japan Tour");
  basecharge=35000;
}
void egypt()
{
   FILE *fh;
    fh = fopen("C://Users/dkshi/Downloads/cpminiprojfiles/egypt.txt","r");
  if(fh != NULL )
  {
    char c;
    while((c=fgetc(fh)) != EOF)
     putchar(c);
     fclose(fh);
  }
  strcpy(place, "Egypt Tour");
  basecharge=45000;

}
void ooty()
{
   FILE *fh;
    fh = fopen("C://Users/dkshi/Downloads/cpminiprojfiles/ooty.txt","r");
  if(fh != NULL )
  {
    char c;
    while((c=fgetc(fh)) != EOF)
     putchar(c);
     fclose(fh);
  }
  strcpy(place, "Ooty Tour");
  basecharge=30000;
}
void details()
{
    int i, a;
    char gen[100],val[100];
    system("cls");
    heading();
    printf("\t\t\t\tEnter Number Of Passengers: ");
    scanf("%d", &k);
    printf("\t\t\t\tEnter Date of Departure (DD/MM/YY): ");
    fflush(stdin);
    gets(date);
    for (i = 1; i <= k; i++) {
        printf("\t\t\t\tEnter Passenger %d Name: ",i);
        fflush(stdin);
        gets(val);
        printf("\t\t\t\tEnter Passenger %d Gender: ",i);
        fflush(stdin);
        gets(gen);
        printf("\t\t\t\tEnter Passenger %d Age: ",i);
        fflush(stdin);
        scanf("%d", &a);
        add_node(val, gen, a);
    }
    m:printf("\t\t\t\tEnter your address: ");
    fflush(stdin);
    gets(addr);
    printf("\t\t\t\tEnter your mobile number: ");
    fflush(stdin);
    gets(mobile);
    printf("\t\t\t\tEnter your alternative mobile number: ");
    fflush(stdin);
    gets(mobile1);
    printf("\t\t\t\tEnter a valid email address for booking information: ");
    fflush(stdin);
    gets(eml);
    printf("Do you want to change any details ? Enter 0 to proceed further or 1 to return back\n");
    int r;
    scanf("%d",&r);
    switch(r){
        case 0:{}
        break;
        case 1:{printf("\nWe will now go back to details to edit\n");
        goto m;
        }
    }
}
void add_node(char lol[20],char der[6], int b)
{
    Node *newptr = NULL, *ptr;
    newptr = (Node*)malloc(sizeof(Node));
    strcpy(newptr->name, lol);
    strcpy(newptr->gen, der);
    newptr->age = b;
    newptr->link = NULL;
    if (start == NULL)
        start = newptr;
    else {
        ptr = start;
        while (ptr->link != NULL)
            ptr = ptr->link;
        ptr->link = newptr;
    }
}
void receipt()
{
    system("cls");
    heading();
    int i, b;
    Node* ptr = start;
    printf("\t\t\t\t**Take Screenshot "
           "For Further Use**\n");
    printf("\t\t\t\tTotal number of passengers: %d\n",k);
    for (i = 1; i <= k; i++) {
        printf("\t\t\t\tPassenger %d "
               "Name: ",
               i);
        puts(ptr->name);
        printf("\t\t\t\tPassenger %d "
               "Gender: ",
               i);
        puts(ptr->gen);
        printf("\t\t\t\tPassenger %d "
               "Age: %d\n",
               i, ptr->age);
        ptr = ptr->link;
    }
    printf("\t\t\t\tMobile no.: %s\n",mobile);
    printf("\t\t\t\tAlternative mobile no.: %s\n",mobile1);
    printf("\t\t\t\tAddress: %s\n",addr);
    printf("\t\t\t\tEmail: %s\n\n",eml);
    printf("\t\t\t\tSelected Type: ");
    puts(type);
    printf("\t\t\t\tPackage: ");
    puts(place);
    printf("\t\t\t\tDate: ");
    puts(date);
    if(n<=5){
    b = (basecharge*k)+(sum)+(guideind*guidenum);}
    else
    {b=(basecharge*k)+(sum1)+(guideint*guidenum1);}
    printf("\t\t\t\tTotal Amount: %d\n", b);
    printf("\t\t\t\tDiscounted Amount is: %d",discountamt);
    printf("\n\t\t\t\tThe breakdown of your fees without discount is: ");
    if(n<=5){
    printf("\n\t\t\t\tbase charge(travel+food): %d \n\t\t\t\thotel charges: %d \n\t\t\t\tguide charges: %d",basecharge*k,sum,guideind*guidenum);}
    else{
        printf("\n\t\t\tbase charge(travel+food+other charges): %d \n\t\t\t\thotel charges: %d \n\t\t\t\tguide charges: %d",basecharge*k,sum1,guideint*guidenum1);
    }
    printf("\n\t\t\t\t**Thank You for the "
           "registration**\n");
    printf("\t\t\t\t**We hope you will enjoy your travels with us**\n");
    printf("\t\t\t\t**Welcome to the New India family!**");
}
void storedata(){
    FILE *fh;
    fh = fopen("C://Users/dkshi/Downloads/cpminiprojfiles/storedata.txt","w");
    if(n<=5){
     Node* ptr = start;
    fprintf(fh,"no. of passengers: %d\nbasecharge: %d\ntotalamt: %d\ndiscountamt: %d\ndate: %s\nname: %s\ngender: %s\nage: %d\naddress: %s\nmobile: %d\nmobile1: %s\nemail: %s\nguidenumdays: %d",k,
            basecharge,basecharge+sum+(guideind*guidenum),discountamt,date,ptr->name,ptr->gen,ptr->age,addr,mobile,mobile1,eml,guidenum);
    }
    else{
    Node* ptr = start;
    fprintf(fh,"no. of passengers: %d\nbasecharge: %d\ntotalamt: %d\ndiscountamt: %d\ndate: %s\nname: %s\ngender: %s\nage: %d\naddress: %s\nmobile: %d\nmobile1: %s\nemail: %s\nguidenumdays: %d",k,
            basecharge,basecharge+sum1+(guideint*guidenum1),discountamt,date,ptr->name,ptr->gen,ptr->age,addr,mobile,mobile1,eml,guidenum1);
    }
}



