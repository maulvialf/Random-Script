#include <GLFW/glfw3.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <random>
#define PII 3.14159265
#define xmax 1400
#define xmin 0
#define ymax 980
#define ymin 0
using namespace std;
int xeee[100];
int yeee[100];
int speed[100];

static void error_callback(int error, const char* description)
{
    fputs(description, stderr);
}
static void key_callback(GLFWwindow* window, int key, int scancode, int action, int mods)
{
    if (key == GLFW_KEY_ESCAPE && action == GLFW_PRESS)
        glfwSetWindowShouldClose(window, GL_TRUE);
}

void circle(int x, int y, float jari){
    int N = 300;
    float pX, pY;
    glBegin(GL_POLYGON);
    for(int i = 0; i < N; i++){
        pX = sin(i*2*PII / N);
        pY = cos(i*2*PII / N);
        glVertex2f(x + (pX * jari), y + (pY * jari));
        
    }
    glEnd();
}


void setup_viewport(GLFWwindow* window)
{
    // setting viewports size, projection etc
    float ratio;
    int width, height;
    glfwGetFramebufferSize(window, &width, &height);
    ratio = width / (float) height;
    glViewport(0, 0, width, height);
glShadeModel( GL_SMOOTH );


    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
	glEnable( GL_BLEND );

    glClear(GL_COLOR_BUFFER_BIT);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(xmin, xmax, ymax, ymin, 1.f, -1.f);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}

void pondasi(){
	float gap = 0.05;
	glColor3ub(0xa5,0x2a,0x2a);
    glBegin(GL_POLYGON);
    glVertex2f(-gap,0.01);
    glVertex2f(gap, 0.01);
    glVertex2f(gap,-1);
    glVertex2f(-gap,-1);
    glEnd();

}
#define batas 0.1
void kincir(){
	// kiri

	for (int i = 0; i < 4; ++i)
	{
		glRotatef(90, 0, 0, 1);
		
		glPushMatrix();
		glBegin(GL_POLYGON);
		glColor3ub(0xff, 0x2f, 0x2f);
		glVertex2f(-batas/4,-batas/4);
		glVertex2f(-batas/4,batas/4);
		glVertex2f(-0.75,batas/4);
		glVertex2f(-0.75,-batas/4);
		glEnd();
		glColor3ub(0x2f, 0xff, 0xff);
		
		glBegin(GL_POLYGON);
		glTranslatef(0.9, 0, 0);
		glVertex2f(-batas,-batas);
		glVertex2f(-batas,batas);
		glVertex2f(-0.75,batas);
		glVertex2f(-0.75,-batas);
		glEnd();

		glPopMatrix();
	}

};

void pentul(){
	float s1 = 0.05;
    glBegin(GL_POLYGON);
    for(float i=0; i<6.28; i+=0.01) {
        float x = s1*cos(i);
        float y = s1*sin(i);
        glVertex2f(x,y);
    }
    glEnd();
};

void background(){
	glColor3ub(69, 115, 196);
	glBegin(GL_POLYGON);
	glVertex2f(0, 710);
	glColor3ub(38, 59, 119);
	glVertex2f(0, ymax);
	glVertex2f(xmax, ymax);
	glColor3ub(69, 115, 196);

	glVertex2f(xmax, 710);
	glEnd();
	
	glColor3ub(38, 59, 119);
	glBegin(GL_POLYGON);
	glVertex2f(0, 710);
	glVertex2f(0, 0);

	glVertex2f(xmax, 0);
	glVertex2f(xmax, 710);
	glEnd();
	

}

void atap(){
	glColor3ub(255, 254, 245);
	glBegin(GL_POLYGON);
	glVertex2f(600, 359);
	glVertex2f(1031, 359);
	glVertex2f(1090, 526);
	glVertex2f(779, 526);
	glEnd();

	glColor3ub(255, 254, 245);
	glBegin(GL_POLYGON);
	glVertex2f(218, 553);
	glVertex2f(189, 553);
	glVertex2f(497, 247);
	glVertex2f(497, 277);
	glEnd();


	glColor3ub(69, 115, 196);
	glBegin(GL_POLYGON);
	glVertex2f(497, 247);
	glVertex2f(497, 277);
	
	glVertex2f(769, 553);
	glVertex2f(799, 553);
	glEnd();


}
void atasitem(){
	glBegin(GL_POLYGON);
	glVertex2f(225, 544);
	glVertex2f(261, 544);
	glVertex2f(497, 302);
	glVertex2f(497, 277);
	glEnd();


	glBegin(GL_POLYGON);
	glVertex2f(497, 302);
	glVertex2f(497, 277);
	glVertex2f(769,544);
	glVertex2f(735,544);
	glEnd();
}

void bawahitem(){
	glBegin(GL_POLYGON);
	glVertex2f(289, 508);
	glVertex2f(709, 508);
	glVertex2f(732, 527);
	glVertex2f(271, 527);
	glEnd();
}

void sedow(){
	glColor3ub(19, 15, 26);
	atasitem();
	bawahitem();
}

void buatsegitiga(int kotak[]){
	glBegin(GL_POLYGON);
	glVertex2f(kotak[0], kotak[1]);
	glVertex2f(kotak[2], kotak[3]);
	glVertex2f(kotak[4], kotak[5]);
	glEnd();

};



void buatkotak(int ex, int ey, int panjang, int tinggi){
	glBegin(GL_POLYGON);
	glVertex2f(ex, ey);
	glVertex2f(ex+panjang, ey);
	glVertex2f(ex+panjang, ey+tinggi);
	glVertex2f(ex, ey+tinggi);
	glEnd();


};



void segi3kiri(){
	glColor3ub(40, 35, 50);
	int kotak[6] = {
		291, 511,
		706, 511,
		496, 297
	};
	buatsegitiga(kotak);
	int l, r, inc;
	l = 482;
	r = 516;
	inc = l - 468;	
	glColor3ub(19, 16, 25);
	for (int i = 311; i < 510; i+= 323-311)
	{
		buatkotak(l, i, r-l, 5);
		l -= inc;
		r += inc;
	}

}

void kotak1(){
	glColor3ub(55, 51, 68);
	buatkotak(294, 518, 707-294,821-518);
	glColor3ub(19, 16, 27);
	for (int i = 518; i < 821; i += 12)
	{
		buatkotak(294, i, 707-294, 5);
	}

}

void kotak2(){
	glColor3ub(30, 27, 38);
	buatkotak(700, 526, 1073-700, 817-526);
}

void kotakj1(){
	glColor3ub(240, 226, 179);
	buatkotak(355, 600, 446-355, 10);
}

void kotakkuningluar(){
	glColor3ub(199, 124, 43);
	buatkotak(369, 617, 432-369, 727-617);
}

void kotakj2(){
	glColor3ub(18, 15, 26);
	buatkotak(362, 610, 439-362, 726-610);
}

void kotakkuningdalem(){
	glColor3ub(242, 179, 86);
	buatkotak(382, 626, 431-382, 726-626);

}

void kotgaris(){
	glColor3ub(19, 16, 27);
	buatkotak(369, 642, 432-369, 647-642);

}

void kotgaris2(){
	glColor3ub(19, 16, 27);
	buatkotak(398, 615, 404-398, 728-615);
}

void jenkiri(){
	glColor3ub(70, 115, 198);
	buatkotak(325, 608, 362-325, 726-608);
	
	glColor3ub(39, 35, 50);

	for (int i = 612+5; i < 716; i+=4)
	{
		buatkotak(332, i, 359-332, 2);
	}
}


void jenkanan(){
	glPushMatrix();
	glTranslated(439-325,0,0);
	jenkiri();
	glPopMatrix();
}

void jendela(){
	kotakj1();
	kotakj2();
	kotakkuningluar();
	kotakkuningdalem();
	kotgaris();
	kotgaris2();
	jenkiri();
	jenkanan();
}

void sedow2(){
	glColor3ub(16, 13, 22);
	for (int i = 536; i < 813; i += 548-536)
	{
		buatkotak(708, i, 1073-708, 547-551);
	}

}

void dinding(){
	kotak2();
	kotak1();
	sedow();
	sedow2();
	segi3kiri();
}



void jendelalagi(){
	glPushMatrix();
	glTranslated(563-363, 0, 0);
	jendela();	
	glPopMatrix();

	glPushMatrix();
	glTranslated(563-469, 486-730+10, 0);
	jendela();	
	glPopMatrix();

}


void jendelalagi2(){
	glPushMatrix();
	glTranslated(873-325,707-731,0);
	jendela();
	glPopMatrix();
}

void pintu(){
	glColor3ub(155, 144, 114);
	buatkotak(705, 782, 864-705, 797-782);
	buatkotak(705, 782+15+1, 864-705+15, 797-782);
	buatkotak(705, 782+15+15+1+1, 864-705+15+15, 797-782);


	glColor3ub(44, 65, 112);
	buatkotak(741, 625, 828-725, 782-625);
	glColor3ub(155, 144, 114);
	
	buatkotak(740-5, 612, 838-731+10, 625-612);

	glColor3ub(12, 11, 19);
	circle(762, 712, 8);

	buatkotak(749, 639, 821-749, 2);
	buatkotak(749, 769, 821-749, 2);

	buatkotak(749, 639, 2, 769-639);
	buatkotak(821, 639, 2, 769-639);

}

void cerobong(){
	glColor3ub(39, 35, 50);
	buatkotak(327, 295, 383-327 ,315-295);
	glColor3ub(39, 35, 50);
	buatkotak(341, 313,373-341 ,395-313);



	// shadow
	glColor3ub(29, 25, 39);

	glBegin(GL_POLYGON);
	glVertex2f(340+3, 312);
	glVertex2f(340+3, 321);
	glVertex2f(375-3, 329);
	glVertex2f(375-3, 312);
	glEnd();


};

void cerobong2(){
	glPushMatrix();
	glTranslated(910-327, 0, 0);
	cerobong();
	glPopMatrix();
}



void pagar(){
	glColor3ub(231, 230, 202);
	glBegin(GL_POLYGON);
	glVertex2f(152, 664);
	glVertex2f(161, 658);
	glVertex2f(171, 663);
	glVertex2f(171, 815);
	glVertex2f(152, 815);
	glEnd();

	

}

void another_pager(){
	glPushMatrix();
	int inc = 0;
	for (int i = 152; i < 1360; i += 174-152)
	{
		inc = 174-152;
		glTranslated(inc, 0, 0);
		pagar();
	}
	glPopMatrix();
	buatkotak(144, 685, 1398-144,5);
}

void jendelapintu(){
	glColor3ub(255, 255, 253);
	glBegin(GL_POLYGON);
	glVertex2f(718, 358);
	glVertex2f(740, 363);
	glVertex2f(808, 296);
	glVertex2f(808, 303);
	glEnd();	
	
	glColor3ub(69, 116, 198);
	glBegin(GL_POLYGON);
	glVertex2f(808, 296);
	glVertex2f(808, 303);
	glVertex2f(895-5, 363);
	glVertex2f(907, 363);
	glEnd();	

	glColor3ub(54, 51, 68);
	buatkotak(750, 360, 866-750, 467-360+5);


	// jendela
	glPushMatrix();
	glTranslated(741-325-5-3, 457-729+100+85+3, 0);
	glScaled(1, 0.75, 0);
	jendela();
	glPopMatrix();
	int kotak[] = {754-4, 355, 808, 313-4, 862+4, 355};
	buatsegitiga(kotak);

	glColor3ub(18, 14, 28);
	glBegin(GL_POLYGON);
	glVertex2f(746, 363);
	glVertex2f(726, 363);
	glVertex2f(808, 303);
	glVertex2f(808, 312);
	glEnd();	

	glColor3ub(25, 21, 35);
	buatkotak(747, 355, 870-747, 360-355);
	
	// glColor3ub(63, 114, 195);
	glBegin(GL_POLYGON);
	glVertex2f(808, 303);
	glVertex2f(808, 312);
	glVertex2f(872, 363);
	glVertex2f(894, 363);
	glEnd();	

	
}

void atapsedow(){
	glColor4ub(0, 0, 0, 30);
	glBegin(GL_POLYGON);
	glVertex2f(610-8, 358);
	glVertex2f(635, 358);
	glVertex2f(910, 527);
	glVertex2f(783-8, 527);
	glEnd();

	glBegin(GL_POLYGON);
	glVertex2f(866, 359);
	glVertex2f(905, 363);
	glVertex2f(986, 468);
	glVertex2f(867, 468);
	glEnd();
}

void asep(){
	glColor3ub(100, 114, 149);
	circle(352, 266+4, 352-321);
	circle(336, 227, 352-321-3);
	circle(367, 205, 352-321-3-4);
	circle(367, 205, 352-321-3-4);
	circle(351, 182, 352-321-3-4-4);
	circle(331, 156, 352-321-3-4-4);
	circle(341, 135, 352-321-3-4-4);

	glPushMatrix();
	glTranslated(913-321+40+20, 70,0);
	glScaled(0.8, 0.8, 0);
	circle(352, 266+4, 352-321);
	circle(336, 227, 352-321-3);
	circle(367, 205, 352-321-3-4);
	circle(367, 205, 352-321-3-4);
	circle(351, 182, 352-321-3-4-4);
	circle(331, 156, 352-321-3-4-4);
	circle(341, 135, 352-321-3-4-4);

	glPopMatrix();
}

void bulan(){
	glColor3ub(252, 248, 200);
	circle(154, 145, 154-68);
	
	glColor3ub(222, 217, 179);
	circle(112, 96, 15);


	glColor3ub(222, 217, 179);
	circle(95, 129, 10);

	glColor3ub(39, 59, 120);
	circle(219, 162, 154-68);

}

void temboksedow(){
	glColor4ub(0, 0, 0, 50);
	glBegin(GL_POLYGON);
	glVertex2f(297, 507);
	glVertex2f(356, 507);
	glVertex2f(494, 304);
	glEnd();

	glBegin(GL_POLYGON);
	glVertex2f(494, 304);
	glVertex2f(669, 507);
	glVertex2f(700, 507);
	glEnd();

	glColor4ub(0, 0, 0, 80);

	glBegin(GL_POLYGON);
	glVertex2f(292, 528);
	glVertex2f(292, 541);
	glVertex2f(705, 583);
	glVertex2f(705, 528);
	glEnd();


	glColor4ub(0, 0, 0, 80);

	glBegin(GL_POLYGON);
	glVertex2f(933, 820);
	glVertex2f(799, 525);
	glVertex2f(705, 523);
	glVertex2f(705, 820);
	glEnd();

}

void particle(int x, int y, int r){
	
	glPushMatrix();
	glTranslated(x, y, 0);
	for (int i = 0; i < 10; ++i)
	{
		glPushMatrix();
		glRotatef(i*45, 0, 0, 1);
		glBegin(GL_POLYGON);
		glVertex2f(-r, 0);
		glVertex2f(0, 0+2);
		glVertex2f(r, 0);
		glVertex2f(0, 0-2);
		glEnd();
		glPopMatrix();
	}

	glPopMatrix();
}

void snow(){
	
	// glColor3ub(255, 255, 255);

	glColor4ub(255, 255, 255, 50);
	for (int i = 0; i < 25; ++i)
	{
		particle(xeee[i], yeee[i], 25);
		yeee[i] += speed[i];	
		yeee[i] %= ymax;
	}
	
}

void display(){
	background();
	pagar();
	another_pager();
	asep();
	bulan();
	cerobong();
	cerobong2();
	dinding();
	atap();
	temboksedow();
	jendela();
	jendelalagi();
	jendelalagi2();
	pintu();	
	jendelapintu();
	atapsedow();
	snow();
} 

int main(int argc, char const *argv[])
{
	GLFWwindow* window;
	if (!glfwInit()) exit(EXIT_FAILURE);
	srand(time(NULL));
	
	for (int i = 0; i < 100; ++i)
	{
		xeee[i] = rand() % xmax;
		yeee[i] = rand() % ymax;
		speed[i] = (rand() % 3) + 1;
	}

	window = glfwCreateWindow(xmax*0.5, ymax*0.5, "Rumah", NULL, NULL);

	if (!window)
	{
	    glfwTerminate();
	    exit(EXIT_FAILURE);
	}

	glfwMakeContextCurrent(window);
	glfwSwapInterval(1);
	glfwSetKeyCallback(window, key_callback);
	
	while (!glfwWindowShouldClose(window))
	{
	    setup_viewport(window);
	    display();
	    glfwSwapBuffers(window);
	    glfwPollEvents();
	}
	glfwDestroyWindow(window);
	glfwTerminate();

	exit(EXIT_SUCCESS);	
	return 0;
}