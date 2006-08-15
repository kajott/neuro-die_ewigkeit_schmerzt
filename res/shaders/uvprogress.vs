uniform float time;
const float width = 80.0;

void main()
{	
	vec4 tc = gl_MultiTexCoord0;
	
	if (time <= 0.0)
	{
		tc.x += 0.6;
	}
	else if (time >= 1.0)
	{
		tc.x -= 0.6;
	}	
	else
	{
		tc.x = (tc.x - time) * width;
	}
	
	if (tc.x<-4.0) tc.x=-4.0;
	else if (tc.x>4.0) tc.x=4.0;

	gl_TexCoord[0] = tc;
}
