login_page_url = 'https://account.blizzard.cn/battlenet/login?inner_client_id=ow&inner_redirect_uri=https%3A%2F%2Fow.blizzard.cn%2Fbattlenet%2Flogin%3Fredirect_url%3Dhttps%253A%252F%252Fow.blizzard.cn%252Fcareer%252F'
login_data_url = 'https://www.battlenet.com.cn/login/zh/?ref=https://www.battlenet.com.cn/oauth/authorize?client_id%3Dnetease-wow-site%26response_type%3Dcode%26scope%3Daccount.basic+account.full+wow.profile+commerce.entitlements+wow.cn+commerce.entitlements.privileged%26redirect_uri%3Dhttps%253A%252F%252Faccount.blizzard.cn%252Fbattlenet%252Flogin%253Finner_client_id%253Dow%2526inner_redirect_uri%253Dhttps%25253A%25252F%25252Fow.blizzard.cn%25252Fbattlenet%25252Flogin%25253Fredirect_url%25253Dhttps%2525253A%2525252F%2525252Fow.blizzard.cn%2525252Fcareer%2525252F&app=oauth'

svg_template = """
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 400 232">
  <defs>
    <style>
      .cls-1 {
        fill: #f2f1ed;
      }

      .cls-2 {
        fill: #ed891d;
      }

      .cls-13, .cls-3 {
        fill: #3d3e7c;
      }

      .cls-4 {
        fill: none;
        stroke: #fff;
        stroke-miterlimit: 10;
      }

      .cls-5 {
        font-size: 10.57px;
      }

      .cls-12, .cls-5, .cls-6, .cls-7, .cls-9 {
        fill: #f0edf2;
      }

      .cls-12, .cls-13, .cls-16, .cls-5, .cls-7, .cls-9 {
        font-family: BebasNeue-Regular, Bebas Neue, MicrosoftYaHei, Microsoft YaHei;
      }

      .cls-7 {
        font-size: 38px;
      }

      .cls-8 {
        letter-spacing: -0.09em;
      }

      .cls-9 {
        font-size: 12.25px;
      }

      .cls-10, .cls-11 {
        fill: #293650;
      }

      .cls-11 {
        fill-rule: evenodd;
      }

      .cls-12, .cls-13 {
        font-size: 19.68px;
      }

      .cls-14 {
        letter-spacing: 0em;
      }

      .cls-15 {
        letter-spacing: -0.05em;
      }

      .cls-16 {
        font-size: 26px;
      }

      .cls-17 {
        font-size: 10px;
        font-family: MicrosoftYaHei, Microsoft YaHei;
      }
      
      #fix1 {
        stroke-dasharray: {1length}, 100; 
        stroke-dashoffset: 0;
        stroke: #f19512;
        stroke-width: 2px;
      }

      #fix2 {
        stroke-dasharray: {2length}, 100; 
        stroke-dashoffset: -{1length};
        stroke: #c81af5;
        stroke-width: 2px;
      }

      #fix3 {
        stroke-dasharray: {3length}, 100; 
        stroke-dashoffset: -{12length};
        stroke: #40ce44;
        stroke-width: 2px;
      }
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
      <image width="256" height="256" transform="translate(254 2) scale(0.18)" xlink:href="level.png"/>
      <image width="256" height="128" transform="translate(255 24) scale(0.17)" xlink:href="level_star.png"/>
      <text id="等级-3" data-name="等级" class="cls-9" transform="translate(268 28.63) scale(1.11 1)">{level}</text>
    </g>
  </g>
  <g id="中栏">
    <g id="分数">
      <text class="cls-7" transform="matrix(0.97, 0, -0.26, 0.97, 40.37, 110.51)">{trating}</text>
      <text class="cls-7" transform="matrix(0.97, 0, -0.26, 0.97, 310.37, 110.96)">{crating}</text>
      <text class="cls-7" transform="matrix(0.97, 0, -0.26, 0.97, 176.37, 110.51)">{nrating}</text>
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
