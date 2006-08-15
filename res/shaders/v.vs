void main()
{	
	gl_Position = ftransform();	
	/*
	vec4 v = gl_ModelViewProjectionMatrix * gl_Vertex;
	gl_Position = v;	
	*/
}
