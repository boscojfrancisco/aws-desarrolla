import re

with open('aws_chaco.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Line 336
lines[335] = lines[335].replace('¿Qué es AWS Entrena Argentina?', '¿Qué es AWS Desarrolla?')

# Line 341
# It contains style and then <p>
part1, part2 = lines[340].split('</style>', 1)
new_p = """				<p style="margin-bottom: 1rem; color: #3c3c3c; font-family: 'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'; font-size: 16px; text-align: left;">El Gobierno de la Provincia del Chaco, en articulación con la empresa tecnológica Amazon Web Services, impulsa el programa AWS Desarrolla, una iniciativa destinada a fortalecer el ecosistema tecnológico provincial mediante el acceso a infraestructura digital en la nube, capacitación y acompañamiento técnico. <br><br>El programa permite que emprendedores, startups, pymes, instituciones y organismos públicos del Chaco puedan desarrollar, probar y escalar soluciones digitales utilizando tecnología cloud de nivel internacional, sin necesidad de inversión inicial en equipamiento o servidores.</p><div>&nbsp;</div>						</div>\n"""
lines[340] = part1 + '</style>' + new_p

# Line 355
lines[354] = lines[354].replace('INSCRIPCIÓN Y MODALIDAD', '¿CÓMO PARTICIPAR?')

# Line 359
lines[358] = """							<p><span style="font-weight: 400; color: #000000;">Las personas u organizaciones interesadas podrán postular sus proyectos tecnológicos para acceder a los beneficios del programa AWS Desarrolla. Se priorizan iniciativas que desarrollen productos tecnológicos, utilicen o prevean utilizar AWS y presenten potencial de crecimiento o impacto.</span></p>						</div>\n"""

# Line 364
lines[363] = lines[363].replace('https://argentina.awsentrena.com/chaco', 'https://argentina.awsentrena.com/#/libraries?id=772a7a2d-10f3-4e7f-981c-cdd5a981af26')

# Line 366
lines[365] = lines[365].replace('Inscribite aquí', 'Postulate aquí')

# Line 382
lines[381] = lines[381].replace('VAS A PODER APRENDER SOBRE:', 'CONOCÉ MÁS SOBRE EL PROGRAMA:')

# Replace the accordion items (lines 389 to 598 is lines[388:598])
accordion_html = """							<details id="e-n-accordion-item-2230" class="e-n-accordion-item e-normal" open>
					<summary class='e-n-accordion-item-title'>
						<span class='e-n-accordion-item-title-header'><div class="e-n-accordion-item-title-text"> ¿Qué permite hacer AWS Desarrolla? </div></span>
								<span class='e-n-accordion-item-title-icon'>
			<span class='e-opened' ><i aria-hidden="true" class="fas fa-minus"></i></span>
			<span class='e-closed'><i aria-hidden="true" class="fas fa-plus"></i></span>
		</span>
							</summary>
					<div class="elementor-element elementor-element-1dbad0e e-con-full e-flex e-con" data-id="1dbad0e" data-element_type="container" data-settings="{&quot;content_width&quot;:&quot;full&quot;}">
				<div class="elementor-element elementor-element-2d854c5 elementor-widget elementor-widget-text-editor" data-id="2d854c5" data-element_type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
							<p>A través de créditos promocionales y servicios AWS, los proyectos pueden:</p>
<ul>
<li>Desarrollar aplicaciones web y móviles</li>
<li>Crear plataformas y servicios digitales</li>
<li>Implementar bases de datos y almacenamiento en la nube</li>
<li>Incorporar analítica de datos e inteligencia artificial</li>
<li>Escalar soluciones tecnológicas según demanda</li>
<li>Desarrollar prototipos o productos mínimos viables (MVP)</li>
</ul>						</div>
				</div>
				</div>
						</details>
							<details id="e-n-accordion-item-2231" class="e-n-accordion-item e-normal" >
					<summary class='e-n-accordion-item-title'>
						<span class='e-n-accordion-item-title-header'><div class="e-n-accordion-item-title-text"> Objetivos del programa </div></span>
								<span class='e-n-accordion-item-title-icon'>
			<span class='e-opened' ><i aria-hidden="true" class="fas fa-minus"></i></span>
			<span class='e-closed'><i aria-hidden="true" class="fas fa-plus"></i></span>
		</span>
							</summary>
					<div class="elementor-element elementor-element-7e45398 e-con-full e-flex e-con" data-id="7e45398" data-element_type="container" data-settings="{&quot;content_width&quot;:&quot;full&quot;}">
				<div class="elementor-element elementor-element-4ae7627 elementor-widget elementor-widget-text-editor" data-id="4ae7627" data-element_type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
<ul>
<li>Promover el desarrollo de soluciones digitales chaqueñas</li>
<li>Fortalecer el ecosistema de innovación y economía del conocimiento provincial</li>
<li>Reducir barreras de acceso a infraestructura tecnológica</li>
<li>Impulsar la transformación digital en el sector público y privado</li>
<li>Acompañar el crecimiento de proyectos tecnológicos locales</li>
</ul>						</div>
				</div>
				</div>
						</details>
							<details id="e-n-accordion-item-2232" class="e-n-accordion-item e-normal" >
					<summary class='e-n-accordion-item-title'>
						<span class='e-n-accordion-item-title-header'><div class="e-n-accordion-item-title-text"> ¿Cómo utilizar los créditos AWS? </div></span>
								<span class='e-n-accordion-item-title-icon'>
			<span class='e-opened' ><i aria-hidden="true" class="fas fa-minus"></i></span>
			<span class='e-closed'><i aria-hidden="true" class="fas fa-plus"></i></span>
		</span>
							</summary>
					<div class="elementor-element elementor-element-bb149b3 e-con-full e-flex e-con" data-id="bb149b3" data-element_type="container" data-settings="{&quot;content_width&quot;:&quot;full&quot;}">
				<div class="elementor-element elementor-element-b091894 elementor-widget elementor-widget-text-editor" data-id="b091894" data-element_type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
							<p>Los créditos AWS son fondos promocionales que cubren el uso de servicios cloud dentro de la plataforma.</p>
<p><strong>Proceso:</strong></p>
<ol>
<li>Postulación al programa AWS Desarrolla</li>
<li>Evaluación y aprobación del proyecto</li>
<li>Creación de cuenta en AWS</li>
<li>Acreditación de créditos promocionales</li>
<li>Uso de servicios tecnológicos</li>
<li>Descuento automático del consumo hasta agotar el crédito</li>
</ol>						</div>
				</div>
				</div>
						</details>
							<details id="e-n-accordion-item-2233" class="e-n-accordion-item e-normal" >
					<summary class='e-n-accordion-item-title'>
						<span class='e-n-accordion-item-title-header'><div class="e-n-accordion-item-title-text"> ¿A quién está dirigido? </div></span>
								<span class='e-n-accordion-item-title-icon'>
			<span class='e-opened' ><i aria-hidden="true" class="fas fa-minus"></i></span>
			<span class='e-closed'><i aria-hidden="true" class="fas fa-plus"></i></span>
		</span>
							</summary>
					<div class="elementor-element elementor-element-fa57c22 e-flex e-con-boxed e-con" data-id="fa57c22" data-element_type="container" data-settings="{&quot;content_width&quot;:&quot;boxed&quot;}">
					<div class="e-con-inner">
				<div class="elementor-element elementor-element-1c2a300 elementor-widget elementor-widget-text-editor" data-id="1c2a300" data-element_type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
							<p><strong>El programa está dirigido a:</strong></p>
<ul>
<li>Startups tecnológicas</li>
<li>Emprendedores digitales</li>
<li>Desarrolladores y programadores</li>
<li>Pymes del sector tecnológico</li>
<li>Universidades e instituciones de innovación</li>
<li>Organismos públicos con proyectos digitales</li>
</ul>						</div>
				</div>
					</div>
				</div>
						</details>
"""
lines = lines[:388] + [accordion_html] + lines[598:]

with open('aws_chaco.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
