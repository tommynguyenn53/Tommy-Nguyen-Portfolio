PImage[] textures;
Ball[] balls;
int texturePoolSize = 3;

void setup() {
  size(800, 600, P3D);
  
  textures = new PImage[texturePoolSize];
  textures[0] = loadImage("data/texture1.png");
  textures[1] = loadImage("data/texture2.png");
  textures[2] = loadImage("data/texture3.png");
  
  balls = new Ball[0];
}

void draw() {
  background(200);
  lights();
  
  // Draw the 6 walls
  drawWalls();
  
  // Update and display all balls
  for (int i = 0; i < balls.length; i++) {
    balls[i].update();
    balls[i].display();
  }
}

void drawWalls() {
  stroke(0);
  fill(150, 150, 150, 50);
  
  pushMatrix();
  translate(width/2, height/2, 0);
  box(width, height, 5);
  popMatrix();
  
  pushMatrix();
  translate(width/2, height/2, -500);
  box(width, height, 5);
  popMatrix();
  
  pushMatrix();
  translate(0, height/2, -250);
  rotateY(HALF_PI);
  box(500, height, 5);
  popMatrix();
  
  pushMatrix();
  translate(width, height/2, -250);
  rotateY(HALF_PI);
  box(500, height, 5);
  popMatrix();
  
  pushMatrix();
  translate(width/2, height, -250);
  rotateX(HALF_PI);
  box(width, 500, 5);
  popMatrix();
  
  pushMatrix();
  translate(width/2, 0, -250);
  rotateX(HALF_PI);
  box(width, 500, 5);
  popMatrix();
}

void mousePressed() {
  PImage randomTexture = textures[int(random(texturePoolSize))];
  Ball newBall = new Ball(mouseX, mouseY, randomTexture);

  balls = (Ball[]) append(balls, newBall);
}

class Ball {
  PVector position;
  PVector velocity;
  PImage texture;
  float radius;
  float gravity;
  float spinSpeed;
  
  Ball(float x, float y, PImage tex) {
    position = new PVector(x, y, 0);
    velocity = PVector.random2D();
    velocity.mult(5); 
    texture = tex;
    radius = 20;
    gravity = 0.1;
    spinSpeed = random(0.01, 0.05);
  }
  
  void update() {
    velocity.y += gravity;
    
    position.add(velocity);
    
    checkBounce();
    
    velocity.mult(0.99);
  }
  
  void checkBounce() {
    if (position.y + radius >= height) {
      position.y = height - radius;
      velocity.y *= -0.8;
    }
    
    if (position.y - radius <= 0) {
      position.y = radius;
      velocity.y *= -0.8;
    }
    
    if (position.x - radius <= 0) {
      position.x = radius;
      velocity.x *= -0.8;
    }
    
    if (position.x + radius >= width) {
      position.x = width - radius;
      velocity.x *= -0.8;
    }
    
    if (position.z + radius >= 0) {
      position.z = radius;
      velocity.z *= -0.8;
    }
    
    if (position.z - radius <= -500) {
      position.z = -500 + radius;
      velocity.z *= -0.8;
    }
  }
  
  void display() {
    pushMatrix();
    translate(position.x, position.y, position.z);
    rotateY(frameCount * spinSpeed);
    rotateX(frameCount * spinSpeed);
    
    noStroke();
    texture(texture);
    sphere(radius); 
    popMatrix();
  }
}
