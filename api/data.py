login_page_url = 'https://account.blizzard.cn/battlenet/login?inner_client_id=ow&inner_redirect_uri=https%3A%2F%2Fow.blizzard.cn%2Fbattlenet%2Flogin%3Fredirect_url%3Dhttps%253A%252F%252Fow.blizzard.cn%252Fcareer%252F'
login_data_url = 'https://www.battlenet.com.cn/login/zh/?ref=https://www.battlenet.com.cn/oauth/authorize?client_id%3Dnetease-wow-site%26response_type%3Dcode%26scope%3Daccount.basic+account.full+wow.profile+commerce.entitlements+wow.cn+commerce.entitlements.privileged%26redirect_uri%3Dhttps%253A%252F%252Faccount.blizzard.cn%252Fbattlenet%252Flogin%253Finner_client_id%253Dow%2526inner_redirect_uri%253Dhttps%25253A%25252F%25252Fow.blizzard.cn%25252Fbattlenet%25252Flogin%25253Fredirect_url%25253Dhttps%2525253A%2525252F%2525252Fow.blizzard.cn%2525252Fcareer%2525252F&app=oauth'

svg_template = """
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 400 232">
  <defs>
    <style>
      .cls-1 {{
        fill: #f2f1ed;
      }}

      .cls-2 {{
        fill: #ed891d;
      }}

      .cls-13, .cls-3 {{
        fill: #3d3e7c;
      }}

      .cls-4 {{
        fill: none;
        stroke: #fff;
        stroke-miterlimit: 10;
      }}

      .cls-5 {{
        font-size: 10.57px;
      }}

      .cls-12, .cls-5, .cls-6, .cls-7, .cls-9 {{
        fill: #f0edf2;
      }}

      .cls-12, .cls-13, .cls-16, .cls-5, .cls-7, .cls-9 {{
        font-family: BebasNeue-Regular, Bebas Neue, MicrosoftYaHei, Microsoft YaHei;
      }}

      .cls-7 {{
        font-size: 38px;
      }}

      .cls-8 {{
        letter-spacing: -0.09em;
      }}

      .cls-9 {{
        font-size: 12.25px;
      }}

      .cls-10, .cls-11 {{
        fill: #293650;
      }}

      .cls-11 {{
        fill-rule: evenodd;
      }}

      .cls-12, .cls-13 {{
        font-size: 19.68px;
      }}

      .cls-14 {{
        letter-spacing: 0em;
      }}

      .cls-15 {{
        letter-spacing: -0.05em;
      }}

      .cls-16 {{
        font-size: 26px;
      }}

      .cls-17 {{
        font-size: 10px;
        font-family: MicrosoftYaHei, Microsoft YaHei;
      }}
      
      #fix1 {{
        stroke-dasharray: {length1}, 100; 
        stroke-dashoffset: 0;
        stroke: #f19512;
        stroke-width: 2px;
      }}

      #fix2 {{
        stroke-dasharray: {length2}, 100; 
        stroke-dashoffset: -{length1};
        stroke: #c81af5;
        stroke-width: 2px;
      }}

      #fix3 {{
        stroke-dasharray: {length3}, 100; 
        stroke-dashoffset: -{length12};
        stroke: #40ce44;
        stroke-width: 2px;
      }}
    </style>
  </defs>
  <g id="背景">
    <g>
      <rect class="cls-1" y="147.64" width="400" height="84.36"/>
      <rect class="cls-2" y="47.45" width="400" height="100.18"/>
      <rect class="cls-3" width="400" height="47.45"/>
    </g>
  </g>
  <g id="顶栏">
    <g id="赞赏等级">
      <circle id="fix1" class="cls-4" cx="351" cy="25" r="7.91"/>
      <circle id="fix2" class="cls-4" cx="351" cy="25" r="7.91"/>
      <circle id="fix3" class="cls-4" cx="351" cy="25" r="7.91"/>
      <text id="等级" class="cls-5" transform="translate(348.5 28.99) scale(1.11 1)">{endorsementlevel}</text>
      {endorsementicon}
    </g>
    <g id="玩家名">
      <image width="128" height="128" transform="translate(5 7) scale(0.27)" xlink:href="{avatar}"/>
      <text class="cls-7" transform="matrix(0.97, 0, -0.26, 0.97, 50.22, 38.69)">{playername}</text>
    </g>
    <g id="等级-2" data-name="等级">
      <image width="256" height="256" transform="translate(254 2) scale(0.18)" xlink:href="{levelimg}"/>
      <image width="256" height="128" transform="translate(255 24) scale(0.17)" xlink:href="{levelstarimg}"/>
      <text id="等级-3" data-name="等级" class="cls-9" transform="translate(268 28.63) scale(1.11 1)">{level}</text>
    </g>
  </g>
  <g id="中栏">
    <g id="分数">
      <text class="cls-7" transform="matrix(0.97, 0, -0.26, 0.97, 40.37, 110.51)">{trating}</text>
      <text class="cls-7" transform="matrix(0.97, 0, -0.26, 0.97, 310.37, 110.96)">{nrating}</text>
      <text class="cls-7" transform="matrix(0.97, 0, -0.26, 0.97, 176.37, 110.51)">{crating}</text>
    </g>
    <g id="图标">
      <path class="cls-10" d="M30,92.23V97a2.28,2.28,0,0,1-.31,1.23,29.49,29.49,0,0,1-9.08,10.16,1,1,0,0,1-1.23,0,29.6,29.6,0,0,1-9-10A2.89,2.89,0,0,1,10.07,97c0-3,.07-6,0-9-.08-2.23,1.61-2.54,3.08-2.92A29.79,29.79,0,0,1,20.46,84a32.13,32.13,0,0,1,7.23,1.23c1,.31,2.08.69,2.23,1.69.08.85,0,1.7.08,2.54Z" transform="translate(0 2)"/>
      <g>
        <g>
          <path class="cls-10" d="M145.72,104.84h5.16v2.84h-5.16Z" transform="translate(0 2)"/>
          <path class="cls-10" d="M150.81,89.51V89c-.36-3.49-2.54-4.58-2.54-4.58s-2.18,1.09-2.55,4.58v13.88h5.09Z" transform="translate(0 2)"/>
        </g>
        <g>
          <path class="cls-10" d="M153.28,104.84h5.16v2.84h-5.16Z" transform="translate(0 2)"/>
          <path class="cls-10" d="M158.37,89.51V89c-.36-3.49-2.54-4.58-2.54-4.58s-2.18,1.09-2.55,4.58v13.88h5.09Z" transform="translate(0 2)"/>
        </g>
        <g>
          <path class="cls-10" d="M160.84,104.84H166v2.84h-5.16Z" transform="translate(0 2)"/>
          <path class="cls-10" d="M165.93,89.51V89c-.37-3.49-2.55-4.58-2.55-4.58s-2.18,1.09-2.54,4.58v13.88h5.09Z" transform="translate(0 2)"/>
        </g>
      </g>
      <path class="cls-11" d="M298.26,93.21h-4.68V88.54a1.67,1.67,0,0,0-1.68-1.68H288a1.67,1.67,0,0,0-1.69,1.68v4.67h-4.61A1.68,1.68,0,0,0,280,94.89v3.93a1.68,1.68,0,0,0,1.68,1.68h4.68v4.67a1.67,1.67,0,0,0,1.68,1.69H292a1.67,1.67,0,0,0,1.68-1.69V100.5h4.68A1.68,1.68,0,0,0,300,98.82V94.89A1.77,1.77,0,0,0,298.26,93.21Z" transform="translate(0 2)"/>
      <text class="cls-12" transform="matrix(0.93, 0, -0.26, 0.97, 3.83, 66.55)">MMR</text>
    </g>
  </g>
  <g id="底栏">
    <image width="1098" height="449" transform="translate(204 152) scale(0.18)" xlink:href="{heroportraitimage}"/>
    <text class="cls-13" transform="matrix(0.93, 0, -0.26, 0.97, 3.73, 166.89)"><tspan class="cls-14">D</tspan><tspan class="cls-15" x="7.95" y="0">at</tspan><tspan x="21.2" y="0">a</tspan></text>
    <g id="_1" data-name="1">
      <text class="cls-16" transform="matrix(0.93, 0, -0.26, 0.97, 40.48, 175.27)">{winrate}</text>
      <text class="cls-17" transform="matrix(0.93, 0, -0.26, 0.97, 43.56, 186.43)">胜率</text>
    </g>
    <g id="_2" data-name="2">
      <text class="cls-16" transform="matrix(0.93, 0, -0.26, 0.97, 40.18, 215.33)">{winround}</text>
      <text class="cls-17" transform="matrix(0.93, 0, -0.26, 0.97, 43.26, 226.49)">胜场数</text>
    </g>
    <g id="_3" data-name="3">
      <text class="cls-16" transform="matrix(0.93, 0, -0.26, 0.97, 120.18, 175.33)">{kill}</text>
      <text class="cls-17" transform="matrix(0.93, 0, -0.26, 0.97, 123.26, 186.49)">消灭</text>
    </g>
    <g id="_4" data-name="4">
      <text class="cls-16" transform="matrix(0.93, 0, -0.26, 0.97, 120.18, 215.33)">{dead}</text>
      <text class="cls-17" transform="matrix(0.93, 0, -0.26, 0.97, 123.26, 226.49)">阵亡</text>
    </g>
    <g id="_5-2" data-name="5">
      <text class="cls-16" transform="matrix(0.93, 0, -0.26, 0.97, 200.18, 175.33)">{special1}</text>
      <text class="cls-17" transform="matrix(0.93, 0, -0.26, 0.97, 203.26, 186.49)">重力喷涌消灭</text>
    </g>
    <g id="_6" data-name="6">
      <text class="cls-16" transform="matrix(0.93, 0, -0.26, 0.97, 200.18, 215.33)">{special2}</text>
      <text class="cls-17" transform="matrix(0.93, 0, -0.26, 0.97, 203.26, 226.49)">高能消灭</text>
    </g>
  </g>
</svg>
"""

svg_icon_0 = """
<g id="_0" data-name=" 0">
        <path class="cls-6" d="M356,10.41l-.78,1.26a11.89,11.89,0,0,0-8.43,0L346,10.41a13.55,13.55,0,0,0,0,25.18l.78-1.25a11.91,11.91,0,0,0,8.44,0l.78,1.25a13.55,13.55,0,0,0,0-25.18Zm-5,23A10.38,10.38,0,1,1,361.38,23,10.38,10.38,0,0,1,351,33.41h0Z" transform="translate(0 2)"/>
      </g>
"""

svg_icon_1 = """
<g id="_1" data-name=" 1">
        <path class="cls-6" d="M356,10.41l-.78,1.26a11.89,11.89,0,0,0-8.43,0L346,10.41a13.55,13.55,0,0,0,0,25.18l.78-1.25a11.91,11.91,0,0,0,8.44,0l.78,1.25a13.55,13.55,0,0,0,0-25.18Zm-5,23A10.38,10.38,0,1,1,361.38,23,10.38,10.38,0,0,1,351,33.41h0Z" transform="translate(0 2)"/>
      </g>
"""

svg_icon_2 = """
<g id="_2-2" data-name=" 2">
            <path class="cls-6" d="M365.31,23.84h-3.94a10.35,10.35,0,0,1-1.57,4.6,9.74,9.74,0,0,1-.9,1.21c-.13.16-.28.3-.42.45a10.4,10.4,0,0,1-5.49,3v3.28a13.6,13.6,0,0,0,7-3.3l-.94-1.84a11.65,11.65,0,0,0,2-2.63c.1-.18.19-.36.28-.54l1.21-.3,1.15-.29.89-.22.94-.24,1.79-.45-.65-2.71Z" transform="translate(0 2)"/>
            <path class="cls-6" d="M366.68,19l-1.94-.49h-.07l-.44-.13-.46-.12-2.36-.63c-.09-.18-.18-.37-.28-.54a11.65,11.65,0,0,0-2-2.63l.93-1.8a13.6,13.6,0,0,0-7-3.3v3.29a10.4,10.4,0,0,1,5.49,3c.15.15.29.3.43.46a9.64,9.64,0,0,1,.87,1.15,10.35,10.35,0,0,1,1.57,4.6h5.33l.65-2.71Z" transform="translate(0 2)"/>
            <path class="cls-6" d="M342.85,14.5a12,12,0,0,0-2,2.59c-.11.19-.21.39-.31.59l-1.21.3-1.15.29-.89.22-2.75.69.65,2.71h5.54a10.53,10.53,0,0,1,1.58-4.6v-.07a12.78,12.78,0,0,1,.84-1.1l.32-.34a10.25,10.25,0,0,1,5.64-3.13V9.38a13.55,13.55,0,0,0-7.18,3.33Z" transform="translate(0 2)"/>
            <path class="cls-6" d="M343.25,29.65a10.11,10.11,0,0,1-.9-1.17v-.07a10.49,10.49,0,0,1-1.58-4.6h-5.59l-.64,2.74,1.79.45.94.24.89.22,1.15.29,1.21.3c.1.21.21.42.33.62a11.78,11.78,0,0,0,2,2.56L341.93,33a13.53,13.53,0,0,0,7.18,3.36V33.06A10.29,10.29,0,0,1,343.54,30Z" transform="translate(0 2)"/>
          </g>
"""

svg_icon_3 = """
<g id="_3" data-name=" 3">
            <path class="cls-6" d="M359.47,9.75l-.9,1.37-.53.81A12.92,12.92,0,0,1,363.9,22.1l1-.05,1.63-.09A15.54,15.54,0,0,0,359.47,9.75Z" transform="translate(0 2)"/>
            <path class="cls-6" d="M361.08,17a11.66,11.66,0,0,0-5.61-4.9l.87-2.08a13.83,13.83,0,0,0-7.81-.87,14.27,14.27,0,0,0-2.93.86l.87,2.08c-.45.2-.89.41-1.32.65a11.63,11.63,0,0,0-5.68,11.56l-2.27.31a14.07,14.07,0,0,0,5.36,9.32L344,32a11.6,11.6,0,0,0,12.87.84,10.84,10.84,0,0,0,1.22-.82l1.39,1.82a13.75,13.75,0,0,0,5.38-9.34l-2.24-.28A11.61,11.61,0,0,0,361.08,17ZM357.26,31a10.34,10.34,0,1,1,3.27-4.23A10.36,10.36,0,0,1,357.26,31Z" transform="translate(0 2)"/>
            <path class="cls-6" d="M343.94,11.93l-.47-.8-.94-1.37A15.51,15.51,0,0,0,335.47,22l1.63.09,1,.05A12.93,12.93,0,0,1,343.94,11.93Z" transform="translate(0 2)"/>
            <path class="cls-6" d="M356.86,34.31a12.86,12.86,0,0,1-11.74,0l-.44.86L344,36.62a15.51,15.51,0,0,0,14.1,0l-.74-1.46Z" transform="translate(0 2)"/>
          </g>
"""

svg_icon_4 = """
<g id="_4" data-name=" 4">
            <path class="cls-6" d="M346.3,10.13l.4.17,1,.4-.19,1-.28,1.52a10.3,10.3,0,0,1,7.68,0l-.28-1.52-.19-1,1-.4.4-.17a13.46,13.46,0,0,0-9.48,0Z" transform="translate(0 2)"/>
            <path class="cls-6" d="M362.42,27.71l-2.47.46a9.6,9.6,0,0,1-.66,1l1,1.85-1.09,1.09-1.85-1a9.6,9.6,0,0,1-1,.66l-.46,2.47,1.54.64,6,2.51,2.08-2.12-2.51-6Z" transform="translate(0 2)"/>
            <path class="cls-6" d="M362.19,26.44l1-.19.4,1,.17.4a13.46,13.46,0,0,0,0-9.48l-.17.4-.4,1-1-.19-1.52-.28a10.3,10.3,0,0,1,0,7.68Z" transform="translate(0 2)"/>
            <path class="cls-6" d="M354.41,35.05l.19-1,.28-1.52a10.3,10.3,0,0,1-7.68,0l.31,1.52.19,1-1,.4-.4.17a13.46,13.46,0,0,0,9.48,0l-.4-.17Z" transform="translate(0 2)"/>
            <path class="cls-6" d="M339.89,19.35l-1,.19-.4-1-.17-.4a13.46,13.46,0,0,0,0,9.48l.17-.4.4-1,1,.19,1.52.28a10.3,10.3,0,0,1,0-7.68Z" transform="translate(0 2)"/>
            <path class="cls-6" d="M345.75,31.79v-.17l-.44-.27c-.15-.09-.3-.16-.44-.26h-.06l-1.85,1L341.87,31l1-1.85V29.1a7.14,7.14,0,0,1-.52-.89h-.17l-2.47-.46L339,29.26l-2.53,6,2.14,2.09,6-2.51,1.54-.64L346,32.88Z" transform="translate(0 2)"/>
            <path class="cls-6" d="M338.63,8.35l-2.12,2.11,2.51,6,.64,1.54,2.47-.46a9.6,9.6,0,0,1,.66-1l-1-1.85,1.13-1,1.85,1a10.79,10.79,0,0,1,1-.66l.21-1.18.24-1.32-1.56-.67Z" transform="translate(0 2)"/>
            <path class="cls-6" d="M357.31,14.66l2.31-1.42,1.09,1.11L360,15.54l-.69,1.14a9.6,9.6,0,0,1,.66,1l2.47.46.62-1.62,2.51-6-2.1-2.17-6,2.51-1.54.64.46,2.47A9.07,9.07,0,0,1,357.31,14.66Z" transform="translate(0 2)"/>
          </g>
"""

svg_icon_5 = """
<g id="_5" data-name=" 5">
            <path class="cls-6" d="M344.34,29.89l-.24-.26a9.1,9.1,0,0,1-1.16-1.39v0l-2.14,1.24-4.88,2.81-.21,2.06,7.55-2.09.36.29.32.23.16.11.13.09.28.17.37.23.22.13.23.13h.07l.58-2.08.08-.32A9.84,9.84,0,0,1,344.34,29.89Zm-2-2.72-.06-.12c0-.13-.11-.26-.16-.38L342,26.4l-.09-.23v-.11c-.08-.21-.13-.42-.19-.64a1.8,1.8,0,0,0-.07-.22l-.08-.31c-.06-.28-.11-.57-.15-.86V22.82l-.32-.08L339,22.19v1a13.66,13.66,0,0,0,.17,1.68l-5.63,5.47,1.88.85,4.87-2.81Zm3.6-13,.23.22a9.71,9.71,0,0,1,2.05-.87h.06c.22-.07.46-.11.68-.17l.33-.07h.06l.45-.06c.2,0,.4-.06.6-.08v-8l-1.66-1.22-2,7.6-.44.17h-.09l-.49.23-.24.12-.52.28-.21.12-.28.2h0Zm11.45,1.3a9.27,9.27,0,0,1,1.31,1.42l1.65-.41.81,1.47-1.17,1.22a9.75,9.75,0,0,1,.59,1.88l2.09-.55.23-.06,4.1-5.19-1.42-2.36-6.47.93-.16.16-1.52,1.51Zm-18.23,4.9.22.05,2.09.56a3.11,3.11,0,0,1,.11-.68,9.49,9.49,0,0,1,.4-1.17L340.8,18l.8-1.47,1.68.4a9.79,9.79,0,0,1,1.33-1.4L343.09,14l-.17-.17-6.47-.91L335,15.25l4,5.14Zm22.07,9.07-2.1-1.21-.12.15c-.15.2-.3.41-.46.61l-.25.29c-.14.16-.28.31-.43.46l-.33.31-.45.38-.35.28c-.21.15-.42.28-.63.41l-.23.15.09.31.61,2.08.42-.23.14-.07.21-.13.67-.45.27-.2.48-.39,7.56,2.1-.2-2.07ZM363,24.89v-.34a1.7,1.7,0,0,1,0-.45c0-.39.06-.78.06-1.19v-.65l-2.09.55-.32.08a6.5,6.5,0,0,1-.05,1V24a5.1,5.1,0,0,1-.17,1v.11a10.22,10.22,0,0,1-.74,2.07l2.1,1.21,4.86,2.81,1.93-.87Zm-8.78,7.18a10,10,0,0,1-1.87.45l-.46,1.6h-1.7l-.46-1.61q-.6-.09-1.2-.24c-.23-.05-.44-.14-.66-.21l-.59,2.12v.22l2.42,6.11h2.76l2.43-6.07-.06-.26Zm1.68-17.68.23-.23,1.51-1.54-.25-.16-.15-.09h-.13l-.1-.06-.11-.05-.24-.13-.18-.1-.12-.14a6.58,6.58,0,0,0-.78-.29h0l-.23-.09-2-7.62-1.69,1.22v8a8.27,8.27,0,0,1,1,.12l.47.1h.14l.39.1.26.08.25.07.5.19.44.2.57.28.22.11Z" transform="translate(0 2)"/>
          </g>
"""

