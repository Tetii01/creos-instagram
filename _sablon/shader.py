import re, sys, json
from playwright.sync_api import sync_playwright
src=open('/home/claude/tetii01/agentie-website/components/ui/LiquidShader.tsx').read()
frag=re.search(r'const FRAGMENT = /\* glsl \*/ `([\s\S]*?)`;',src).group(1)
vert=re.search(r'const VERTEX = /\* glsl \*/ `([\s\S]*?)`;',src).group(1)
W,H=1080,1440
def render(name, cx, cy, scale, t):
    acc=[1,0x3b/255,0x4e/255]
    deep=[c*0.34 for c in acc]; glow=[(c*(1-0.15)+0.15)*5 for c in acc]
    html=f"""<canvas id=c width={W} height={H} style="width:{W}px;height:{H}px"></canvas><script>
    const gl=document.getElementById('c').getContext('webgl',{{alpha:true,premultipliedAlpha:false,preserveDrawingBuffer:true}});
    function sh(t,s){{const x=gl.createShader(t);gl.shaderSource(x,s);gl.compileShader(x);return x}}
    const p=gl.createProgram();gl.attachShader(p,sh(gl.VERTEX_SHADER,{json.dumps(vert)}));gl.attachShader(p,sh(gl.FRAGMENT_SHADER,{json.dumps(frag)}));gl.linkProgram(p);gl.useProgram(p);
    const b=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,b);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,3,-1,-1,3]),gl.STATIC_DRAW);
    const l=gl.getAttribLocation(p,'position');gl.enableVertexAttribArray(l);gl.vertexAttribPointer(l,2,gl.FLOAT,false,0,0);
    gl.uniform3fv(gl.getUniformLocation(p,'uDeep'),{deep});gl.uniform3fv(gl.getUniformLocation(p,'uGlow'),{glow});
    gl.uniform1f(gl.getUniformLocation(p,'uIntensity'),0.82);gl.uniform2f(gl.getUniformLocation(p,'uCenter'),{cx},{cy});
    gl.uniform1f(gl.getUniformLocation(p,'uScale'),{scale});gl.uniform1f(gl.getUniformLocation(p,'uTime'),{t});
    gl.viewport(0,0,{W},{H});gl.drawArrays(gl.TRIANGLES,0,3);window.done=document.getElementById('c').toDataURL('image/png');
    </script>"""
    with sync_playwright() as pw:
        br=pw.chromium.launch(args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist'])
        pg=br.new_page(viewport={'width':W,'height':H}); pg.set_content(html); pg.wait_for_function('window.done')
        import base64; open(name,'wb').write(base64.b64decode(pg.evaluate('window.done').split(',')[1])); br.close()
# gl coords: origin bottom-left
for t in [3,6,9,12]:
    render(f'assets/glow_t{t}.png', W*0.66, H*0.86, W*0.78, t)
print('ok')
