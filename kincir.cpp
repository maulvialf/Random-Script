#include <GLFW/glfw3.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#define PII 3.1415

//  membuat matahari berada pada titik tengah layar
#define xmin -8 
#define xmax 8
#define ymin -8
#define ymax 8
// g++ -Wall -o "kincir" "kincir.cpp" -lglfw3 -lGL -lX11 -lXi -lXrandr -lXxf86vm -lXinerama -lXcursor -lrt -lm -pthread

using namespace std;

static void error_callback(int error, const char* description)
{
    fputs(description, stderr);
}
static void key_callback(GLFWwindow* window, int key, int scancode, int action, int mods)
{
    if (key == GLFW_KEY_ESCAPE && action == GLFW_PRESS)
        glfwSetWindowShouldClose(window, GL_TRUE);
}


void setup_viewport(GLFWwindow* window)
{
    // setting viewports size, projection etc
    float ratio;
    int width, height;
    glfwGetFramebufferSize(window, &width, &height);
    ratio = width / (float) height;
    glViewport(0, 0, width, height);

    glClear(GL_COLOR_BUFFER_BIT);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(-ratio, ratio, -1.f, 1.f, 1.f, -1.f);
    // glOrtho(xmin, xmax, ymin, ymax, 1.f, -1.f);
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

		// for (float i = -batas; i < batas; )
		// {
			
		// }

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

void display(){
	// glPushMatrix();

	pondasi();

	
	glColor3ub(0xff,0xff,0xff);
	glPushMatrix();
	glRotatef(glfwGetTime()*40,0,0,1);
	kincir();
	glPopMatrix();
	glColor3ub(0xd3,0xd3,0xd3);

	pentul();
} 


int main(int argc, char const *argv[])
{
	GLFWwindow* window;
	if (!glfwInit()) exit(EXIT_FAILURE);

	window = glfwCreateWindow(500, 500, "Kincir", NULL, NULL);

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